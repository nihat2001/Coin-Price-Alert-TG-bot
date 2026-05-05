📈 **BTC Multi-Stage Market Monitoring Bot**

This repository contains the n8n workflow JSON for a dual-architecture Bitcoin monitoring system. It provides both real-time price analysis and conditional threshold alerts via Telegram.

📋 **Features**

Dual-Logic Architecture:

Alert Stream: Specifically filters for high-volatility events (>$85k or <$72k) to ensure you never miss critical movements.

Analysis Stream: Provides a constant 10-minute heartbeat of market status for continuous data tracking.

Automated Normalization: Uses custom JavaScript nodes to parse Coinbase API data and format currency strings.

Real-time Alerts: Instant Telegram notifications with emojis and formatted pricing for high readability.

🚀 **How to Install**

Since this repository only contains the workflow logic, follow these steps to get it running:

**Download the JSON:**

Open the workflow.json file in this repository.

Click the "Raw" button and copy the entire code.

**Import to n8n:**

Open your n8n instance.

Create a new workflow.

Simply Paste (Ctrl+V) the copied JSON code directly into the editor, or go to Workflow Settings > Import from File.

**Configure Credentials:**

Telegram: Create a bot via @BotFather and add your credentials to both Telegram nodes.

Coinbase API: The HTTP nodes are pre-configured for public spot prices; no API key is required unless you hit rate limits.

**Activate:**

The "Schedule Trigger" is set to run every 10 minutes. Click Execute Workflow to test the initial connection.

🛠️ **Tech Stack**

n8n: Workflow automation engine.

Docker: For self-hosted deployment.

JavaScript: For price normalization and conditional logic.

Coinbase API: For real-time BTC-USD market data.

Telegram Bot API: For instant notifications.
