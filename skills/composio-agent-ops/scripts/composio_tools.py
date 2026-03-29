"""
Composio integrations for Hermes Agent.

Provides Linear, Notion, Gmail access via Composio SDK.
"""

import json
import logging
import os
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

try:
    from composio import Composio, Action
    COMPOSIO_AVAILABLE = True
except ImportError:
    COMPOSIO_AVAILABLE = False
    logger.warning("composio-core not installed. Install with: pip install composio-core")


class ComposioAgentTools:
    """Wrapper for Composio integrations."""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize Composio client."""
        if not COMPOSIO_AVAILABLE:
            raise ImportError("composio-core is required. Install with: pip install composio-core")
        
        api_key = api_key or os.getenv("COMPOSIO_API_KEY")
        if not api_key:
            raise ValueError("COMPOSIO_API_KEY not set. Add to ~/.hermes/.env")
        
        self.client = Composio(api_key=api_key)
        self.logger = logger
    
    # ========== LINEAR OPERATIONS ==========
    
    def read_linear_issue(self, issue_id: str) -> Dict[str, Any]:
        """
        Read a Linear issue by ID.
        
        Args:
            issue_id: Linear issue ID (e.g., "ACME-42")
        
        Returns:
            Issue details: {id, title, description, status, assignee, ...}
        """
        try:
            result = self.client.call_action(
                tool="linear",
                action="get_issue",
                params={"issue_id": issue_id}
            )
            return self._format_response(result)
        except Exception as e:
            self.logger.error(f"read_linear_issue failed: {e}")
            return {"error": str(e), "issue_id": issue_id}
    
    def list_linear_issues(self, project_id: Optional[str] = None, 
                          status: Optional[str] = None,
                          assignee: Optional[str] = None) -> Dict[str, Any]:
        """
        List Linear issues with optional filters.
        
        Args:
            project_id: Filter by project (e.g., "ACME")
            status: Filter by status (e.g., "Todo", "In Progress", "Done")
            assignee: Filter by assignee email
        
        Returns:
            List of issues matching filters
        """
        try:
            filters = {}
            if project_id:
                filters["project_id"] = project_id
            if status:
                filters["status"] = status
            if assignee:
                filters["assignee"] = assignee
            
            result = self.client.call_action(
                tool="linear",
                action="list_issues",
                params=filters or {}
            )
            return self._format_response(result)
        except Exception as e:
            self.logger.error(f"list_linear_issues failed: {e}")
            return {"error": str(e), "filters": {"project_id": project_id, "status": status, "assignee": assignee}}
    
    def create_linear_issue(self, project_id: str, title: str, 
                           description: Optional[str] = None,
                           assignee: Optional[str] = None) -> Dict[str, Any]:
        """
        Create a new Linear issue.
        
        Args:
            project_id: Project ID (e.g., "ACME")
            title: Issue title
            description: Issue description (optional)
            assignee: Assignee email (optional)
        
        Returns:
            Created issue details including ID
        """
        try:
            params = {
                "project_id": project_id,
                "title": title
            }
            if description:
                params["description"] = description
            if assignee:
                params["assignee"] = assignee
            
            result = self.client.call_action(
                tool="linear",
                action="create_issue",
                params=params
            )
            return self._format_response(result)
        except Exception as e:
            self.logger.error(f"create_linear_issue failed: {e}")
            return {"error": str(e), "project_id": project_id, "title": title}
    
    # ========== NOTION OPERATIONS ==========
    
    def read_notion_database(self, database_id: str, 
                            filter_rules: Optional[Dict] = None,
                            page_size: int = 10) -> Dict[str, Any]:
        """
        Query a Notion database.
        
        Args:
            database_id: Notion database ID
            filter_rules: Filter criteria (optional)
            page_size: Max results to return
        
        Returns:
            List of database entries/pages
        """
        try:
            params = {
                "database_id": database_id,
                "page_size": page_size
            }
            if filter_rules:
                params["filter"] = filter_rules
            
            result = self.client.call_action(
                tool="notion",
                action="query_database",
                params=params
            )
            return self._format_response(result)
        except Exception as e:
            self.logger.error(f"read_notion_database failed: {e}")
            return {"error": str(e), "database_id": database_id}
    
    def create_notion_entry(self, database_id: str, 
                           properties: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new Notion database entry.
        
        Args:
            database_id: Notion database ID
            properties: Entry properties (key-value pairs matching database schema)
        
        Returns:
            Created entry details including page ID
        """
        try:
            result = self.client.call_action(
                tool="notion",
                action="create_page",
                params={
                    "parent_id": database_id,
                    "properties": properties
                }
            )
            return self._format_response(result)
        except Exception as e:
            self.logger.error(f"create_notion_entry failed: {e}")
            return {"error": str(e), "database_id": database_id}
    
    def update_notion_entry(self, page_id: str, 
                           properties: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a Notion page/entry.
        
        Args:
            page_id: Notion page ID
            properties: Properties to update
        
        Returns:
            Updated page details
        """
        try:
            result = self.client.call_action(
                tool="notion",
                action="update_page",
                params={
                    "page_id": page_id,
                    "properties": properties
                }
            )
            return self._format_response(result)
        except Exception as e:
            self.logger.error(f"update_notion_entry failed: {e}")
            return {"error": str(e), "page_id": page_id}
    
    # ========== GMAIL OPERATIONS ==========
    
    def send_email(self, to: str, subject: str, body: str,
                   cc: Optional[str] = None,
                   bcc: Optional[str] = None) -> Dict[str, Any]:
        """
        Send an email via Gmail.
        
        Args:
            to: Recipient email
            subject: Email subject
            body: Email body (plain text or HTML)
            cc: CC recipients (comma-separated, optional)
            bcc: BCC recipients (comma-separated, optional)
        
        Returns:
            Status: {status: "sent", message_id, ...}
        """
        try:
            params = {
                "to": to,
                "subject": subject,
                "body": body
            }
            if cc:
                params["cc"] = cc
            if bcc:
                params["bcc"] = bcc
            
            result = self.client.call_action(
                tool="gmail",
                action="send_message",
                params=params
            )
            response = self._format_response(result)
            response["status"] = "sent"
            return response
        except Exception as e:
            self.logger.error(f"send_email failed: {e}")
            return {"error": str(e), "to": to, "subject": subject}
    
    def search_email(self, query: str, max_results: int = 10) -> Dict[str, Any]:
        """
        Search emails in Gmail.
        
        Args:
            query: Gmail search query (e.g., "from:user@example.com", "has:attachment")
            max_results: Max emails to return
        
        Returns:
            List of matching emails: {from, to, subject, date, snippet, ...}
        """
        try:
            result = self.client.call_action(
                tool="gmail",
                action="search_messages",
                params={
                    "query": query,
                    "max_results": max_results
                }
            )
            return self._format_response(result)
        except Exception as e:
            self.logger.error(f"search_email failed: {e}")
            return {"error": str(e), "query": query}
    
    def read_email(self, message_id: str) -> Dict[str, Any]:
        """
        Read full email content.
        
        Args:
            message_id: Gmail message ID
        
        Returns:
            Full message: {from, to, subject, body, attachments, ...}
        """
        try:
            result = self.client.call_action(
                tool="gmail",
                action="get_message",
                params={"message_id": message_id}
            )
            return self._format_response(result)
        except Exception as e:
            self.logger.error(f"read_email failed: {e}")
            return {"error": str(e), "message_id": message_id}
    
    # ========== UTILITIES ==========
    
    def check_status(self) -> Dict[str, Any]:
        """
        Check authentication status for all integrations.
        
        Returns:
            {linear: bool, notion: bool, gmail: bool, ...}
        """
        try:
            # Try a simple operation on each tool to verify auth
            status = {
                "composio": "connected"
            }
            
            # Check Linear
            try:
                self.client.call_action(tool="linear", action="list_issues", params={})
                status["linear"] = "authenticated"
            except:
                status["linear"] = "not_authenticated"
            
            # Check Notion
            try:
                self.client.call_action(tool="notion", action="search_pages", params={})
                status["notion"] = "authenticated"
            except:
                status["notion"] = "not_authenticated"
            
            # Check Gmail
            try:
                self.client.call_action(tool="gmail", action="search_messages", params={"query": "is:starred", "max_results": 1})
                status["gmail"] = "authenticated"
            except:
                status["gmail"] = "not_authenticated"
            
            return status
        except Exception as e:
            self.logger.error(f"check_status failed: {e}")
            return {"error": str(e)}
    
    @staticmethod
    def _format_response(response: Any) -> Dict[str, Any]:
        """Format Composio response to JSON-serializable dict."""
        if isinstance(response, dict):
            return response
        elif isinstance(response, str):
            try:
                return json.loads(response)
            except:
                return {"result": response}
        else:
            return {"result": str(response)}


# Singleton instance
_tools_instance = None


def get_tools() -> ComposioAgentTools:
    """Get or create singleton Composio tools instance."""
    global _tools_instance
    if _tools_instance is None:
        _tools_instance = ComposioAgentTools()
    return _tools_instance


# ========== HERMES TOOL HANDLERS ==========
# These are called by the Hermes tool registry

def composio_read_linear_issue(issue_id: str, **kwargs) -> str:
    """Handler for read_linear_issue tool."""
    try:
        tools = get_tools()
        result = tools.read_linear_issue(issue_id)
        return json.dumps(result)
    except Exception as e:
        return json.dumps({"error": str(e)})


def composio_list_linear_issues(project_id: Optional[str] = None,
                                status: Optional[str] = None,
                                assignee: Optional[str] = None, **kwargs) -> str:
    """Handler for list_linear_issues tool."""
    try:
        tools = get_tools()
        result = tools.list_linear_issues(project_id, status, assignee)
        return json.dumps(result)
    except Exception as e:
        return json.dumps({"error": str(e)})


def composio_create_linear_issue(project_id: str, title: str,
                                 description: Optional[str] = None,
                                 assignee: Optional[str] = None, **kwargs) -> str:
    """Handler for create_linear_issue tool."""
    try:
        tools = get_tools()
        result = tools.create_linear_issue(project_id, title, description, assignee)
        return json.dumps(result)
    except Exception as e:
        return json.dumps({"error": str(e)})


def composio_read_notion_database(database_id: str,
                                  filter_rules: Optional[Dict] = None,
                                  page_size: int = 10, **kwargs) -> str:
    """Handler for read_notion_database tool."""
    try:
        tools = get_tools()
        result = tools.read_notion_database(database_id, filter_rules, page_size)
        return json.dumps(result)
    except Exception as e:
        return json.dumps({"error": str(e)})


def composio_create_notion_entry(database_id: str, properties: Dict[str, Any], **kwargs) -> str:
    """Handler for create_notion_entry tool."""
    try:
        tools = get_tools()
        result = tools.create_notion_entry(database_id, properties)
        return json.dumps(result)
    except Exception as e:
        return json.dumps({"error": str(e)})


def composio_send_email(to: str, subject: str, body: str,
                       cc: Optional[str] = None,
                       bcc: Optional[str] = None, **kwargs) -> str:
    """Handler for send_email tool."""
    try:
        tools = get_tools()
        result = tools.send_email(to, subject, body, cc, bcc)
        return json.dumps(result)
    except Exception as e:
        return json.dumps({"error": str(e)})


def composio_search_email(query: str, max_results: int = 10, **kwargs) -> str:
    """Handler for search_email tool."""
    try:
        tools = get_tools()
        result = tools.search_email(query, max_results)
        return json.dumps(result)
    except Exception as e:
        return json.dumps({"error": str(e)})


def composio_check_status(**kwargs) -> str:
    """Handler for check_status tool."""
    try:
        tools = get_tools()
        result = tools.check_status()
        return json.dumps(result)
    except Exception as e:
        return json.dumps({"error": str(e)})
