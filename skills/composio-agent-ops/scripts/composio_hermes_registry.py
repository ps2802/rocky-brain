"""
Register Composio tools with Hermes agent.

This module is imported by hermes-agent/model_tools.py to add Composio tools to the available toolset.
"""

import logging

logger = logging.getLogger(__name__)

# Import the tool handlers
try:
    from composio_tools import (
        composio_read_linear_issue,
        composio_list_linear_issues,
        composio_create_linear_issue,
        composio_read_notion_database,
        composio_create_notion_entry,
        composio_send_email,
        composio_search_email,
        composio_check_status,
    )
    COMPOSIO_AVAILABLE = True
except ImportError:
    COMPOSIO_AVAILABLE = False
    logger.debug("Composio not available or not installed")


def register_composio_tools(registry):
    """
    Register all Composio tools with the Hermes tool registry.
    
    Args:
        registry: Hermes tool registry (tools.registry.registry)
    """
    if not COMPOSIO_AVAILABLE:
        logger.debug("Skipping Composio registration (not available)")
        return
    
    # Linear Tools
    registry.register(
        name="composio_read_linear_issue",
        toolset="agent-operations",
        schema={
            "name": "composio_read_linear_issue",
            "description": "Read a Linear issue by ID. Returns issue details including assignee, status, description, and custom fields.",
            "parameters": {
                "type": "object",
                "properties": {
                    "issue_id": {
                        "type": "string",
                        "description": "Linear issue ID (e.g., 'ACME-42' or 'LUNAR-1')"
                    }
                },
                "required": ["issue_id"]
            }
        },
        handler=lambda args, **kw: composio_read_linear_issue(
            issue_id=args.get("issue_id", ""),
            task_id=kw.get("task_id")
        ),
        requires_env=["COMPOSIO_API_KEY"],
    )
    
    registry.register(
        name="composio_list_linear_issues",
        toolset="agent-operations",
        schema={
            "name": "composio_list_linear_issues",
            "description": "List Linear issues with optional filters by project, status, or assignee.",
            "parameters": {
                "type": "object",
                "properties": {
                    "project_id": {
                        "type": "string",
                        "description": "Filter by project (e.g., 'ACME'). Optional."
                    },
                    "status": {
                        "type": "string",
                        "description": "Filter by status (e.g., 'Todo', 'In Progress', 'Done'). Optional."
                    },
                    "assignee": {
                        "type": "string",
                        "description": "Filter by assignee email. Optional."
                    }
                }
            }
        },
        handler=lambda args, **kw: composio_list_linear_issues(
            project_id=args.get("project_id"),
            status=args.get("status"),
            assignee=args.get("assignee"),
            task_id=kw.get("task_id")
        ),
        requires_env=["COMPOSIO_API_KEY"],
    )
    
    registry.register(
        name="composio_create_linear_issue",
        toolset="agent-operations",
        schema={
            "name": "composio_create_linear_issue",
            "description": "Create a new Linear issue in a project.",
            "parameters": {
                "type": "object",
                "properties": {
                    "project_id": {
                        "type": "string",
                        "description": "Project ID (e.g., 'ACME')"
                    },
                    "title": {
                        "type": "string",
                        "description": "Issue title"
                    },
                    "description": {
                        "type": "string",
                        "description": "Issue description. Optional."
                    },
                    "assignee": {
                        "type": "string",
                        "description": "Assignee email. Optional."
                    }
                },
                "required": ["project_id", "title"]
            }
        },
        handler=lambda args, **kw: composio_create_linear_issue(
            project_id=args.get("project_id", ""),
            title=args.get("title", ""),
            description=args.get("description"),
            assignee=args.get("assignee"),
            task_id=kw.get("task_id")
        ),
        requires_env=["COMPOSIO_API_KEY"],
    )
    
    # Notion Tools
    registry.register(
        name="composio_read_notion_database",
        toolset="agent-operations",
        schema={
            "name": "composio_read_notion_database",
            "description": "Query a Notion database. Returns list of entries/pages matching optional filters.",
            "parameters": {
                "type": "object",
                "properties": {
                    "database_id": {
                        "type": "string",
                        "description": "Notion database ID"
                    },
                    "filter_rules": {
                        "type": "object",
                        "description": "Filter criteria (optional). Example: {'property': 'Status', 'select': {'equals': 'Approved'}}"
                    },
                    "page_size": {
                        "type": "integer",
                        "description": "Max results to return (default: 10)",
                        "default": 10
                    }
                },
                "required": ["database_id"]
            }
        },
        handler=lambda args, **kw: composio_read_notion_database(
            database_id=args.get("database_id", ""),
            filter_rules=args.get("filter_rules"),
            page_size=args.get("page_size", 10),
            task_id=kw.get("task_id")
        ),
        requires_env=["COMPOSIO_API_KEY"],
    )
    
    registry.register(
        name="composio_create_notion_entry",
        toolset="agent-operations",
        schema={
            "name": "composio_create_notion_entry",
            "description": "Create a new entry/row in a Notion database.",
            "parameters": {
                "type": "object",
                "properties": {
                    "database_id": {
                        "type": "string",
                        "description": "Notion database ID"
                    },
                    "properties": {
                        "type": "object",
                        "description": "Entry properties as key-value pairs matching database schema"
                    }
                },
                "required": ["database_id", "properties"]
            }
        },
        handler=lambda args, **kw: composio_create_notion_entry(
            database_id=args.get("database_id", ""),
            properties=args.get("properties", {}),
            task_id=kw.get("task_id")
        ),
        requires_env=["COMPOSIO_API_KEY"],
    )
    
    # Gmail Tools
    registry.register(
        name="composio_send_email",
        toolset="agent-operations",
        schema={
            "name": "composio_send_email",
            "description": "Send an email via Gmail.",
            "parameters": {
                "type": "object",
                "properties": {
                    "to": {
                        "type": "string",
                        "description": "Recipient email address"
                    },
                    "subject": {
                        "type": "string",
                        "description": "Email subject"
                    },
                    "body": {
                        "type": "string",
                        "description": "Email body (plain text or HTML)"
                    },
                    "cc": {
                        "type": "string",
                        "description": "CC recipients (comma-separated). Optional."
                    },
                    "bcc": {
                        "type": "string",
                        "description": "BCC recipients (comma-separated). Optional."
                    }
                },
                "required": ["to", "subject", "body"]
            }
        },
        handler=lambda args, **kw: composio_send_email(
            to=args.get("to", ""),
            subject=args.get("subject", ""),
            body=args.get("body", ""),
            cc=args.get("cc"),
            bcc=args.get("bcc"),
            task_id=kw.get("task_id")
        ),
        requires_env=["COMPOSIO_API_KEY"],
    )
    
    registry.register(
        name="composio_search_email",
        toolset="agent-operations",
        schema={
            "name": "composio_search_email",
            "description": "Search emails in Gmail. Supports Gmail search syntax (from:, has:attachment, is:unread, etc.).",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Gmail search query (e.g., 'from:user@example.com', 'has:attachment', 'is:unread')"
                    },
                    "max_results": {
                        "type": "integer",
                        "description": "Max emails to return (default: 10)",
                        "default": 10
                    }
                },
                "required": ["query"]
            }
        },
        handler=lambda args, **kw: composio_search_email(
            query=args.get("query", ""),
            max_results=args.get("max_results", 10),
            task_id=kw.get("task_id")
        ),
        requires_env=["COMPOSIO_API_KEY"],
    )
    
    # Status Tool
    registry.register(
        name="composio_check_status",
        toolset="agent-operations",
        schema={
            "name": "composio_check_status",
            "description": "Check authentication status for all Composio integrations (Linear, Notion, Gmail).",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        },
        handler=lambda args, **kw: composio_check_status(
            task_id=kw.get("task_id")
        ),
        requires_env=["COMPOSIO_API_KEY"],
    )
    
    logger.info("✓ Registered 8 Composio tools (Linear, Notion, Gmail, Status)")
