{
  "nodes": [
    {
      "parameters": {
        "rule": {
          "interval": [
            {
              "field": "minutes",
              "minutesInterval": 10
            }
          ]
        }
      },
      "type": "n8n-nodes-base.scheduleTrigger",
      "typeVersion": 1.3,
      "position": [
        0,
        0
      ],
      "id": "6e266e4a-fe5b-4294-aecc-eaae3b169af5",
      "name": "Schedule Trigger"
    },
    {
      "parameters": {
        "url": "https://api.coinbase.com/v2/prices/BTC-USD/spot",
        "options": {}
      },
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.4,
      "position": [
        208,
        0
      ],
      "id": "c169fc67-786d-4e18-843d-9287e2de51ef",
      "name": "HTTP Request"
    },
    {
      "parameters": {
        "jsCode": "const price = parseFloat($json.data.amount);\n\nlet status = \"\";\nlet alert = false;\n\nif (price > 85000) {\n    status = \"🚀 High amount!\";\n    alert = true;\n} else if (price < 72000) {\n    status = \"📉 Low amount!\";\n    alert = true;\n} else {\n    status = \"📊 Normal amount.\";\n    alert = false;\n}\n\nreturn {\n    price: price,\n    status: status,\n    alert: alert,\n};"
      },
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [
        416,
        0
      ],
      "id": "614095ba-a9b2-491e-affd-939cd9e82400",
      "name": "Code in JavaScript"
    },
    {
      "parameters": {
        "chatId": "6979411839",
        "text": "=📊 BTC Market Update\n\n💰 Current Price: {{ $json.price.toLocaleString('en-US', { style: 'currency', currency: 'USD' }) }}\n🏷️ Status: {{ $json.status }}\n⏰ Timestamp: {{ $now.toLocaleString() }}",
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        864,
        -128
      ],
      "id": "82bf5d58-e8dc-4ac6-a854-e8c28ecda7ba",
      "name": "Send a text message",
      "webhookId": "a1d4b8a6-81f4-47c6-8bc8-702b3af73cf2",
      "credentials": {
        "telegramApi": {
          "id": "2v6xLPKkn3HD2Rdn",
          "name": "Telegram account 2"
        }
      }
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict",
            "version": 3
          },
          "conditions": [
            {
              "id": "22396635-0414-4009-8369-19812b8feb4c",
              "leftValue": "={{ $json.alert }}",
              "rightValue": true,
              "operator": {
                "type": "boolean",
                "operation": "equals"
              }
            }
          ],
          "combinator": "or"
        },
        "options": {}
      },
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.3,
      "position": [
        624,
        0
      ],
      "id": "a37b70b0-1e7f-4f2b-af8e-524969221122",
      "name": "If"
    },
    {
      "parameters": {
        "rule": {
          "interval": [
            {
              "field": "minutes",
              "minutesInterval": 10
            }
          ]
        }
      },
      "type": "n8n-nodes-base.scheduleTrigger",
      "typeVersion": 1.3,
      "position": [
        0,
        208
      ],
      "id": "a66584b3-635d-4ee6-934d-6e813f9646f9",
      "name": "Schedule Trigger1"
    },
    {
      "parameters": {
        "url": "https://api.coinbase.com/v2/prices/BTC-USD/spot",
        "options": {}
      },
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.4,
      "position": [
        208,
        208
      ],
      "id": "68579993-6ba0-46e5-8d17-f0d75427af38",
      "name": "HTTP Request1"
    },
    {
      "parameters": {
        "jsCode": "const price = parseFloat($json.data.amount);\n\nlet status = \"\";\nlet alert = false;\n\nif (price > 85000) {\n    status = \"🚀 High amount!\";\n    alert = true;\n} else if (price < 72000) {\n    status = \"📉 Low amount!\";\n    alert = true;\n} else {\n    status = \"📊 Normal amount.\";\n    alert = false;\n}\n\nreturn {\n    price: price,\n    status: status,\n    alert: alert,\n};"
      },
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [
        416,
        208
      ],
      "id": "e7a0c176-2212-4227-84ab-878de1bae20c",
      "name": "Code in JavaScript1"
    },
    {
      "parameters": {
        "chatId": "6979411839",
        "text": "=📊 BTC Market Update\n\n💰 Current Price: {{ $json.price.toLocaleString('en-US', { style: 'currency', currency: 'USD' }) }}\n🏷️ Status: {{ $json.status }}\n⏰ Timestamp: {{ $now.toLocaleString() }}",
        "additionalFields": {}
      },
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1.2,
      "position": [
        624,
        208
      ],
      "id": "61b6836f-7dee-498b-b666-150d4c1b34bd",
      "name": "Send a text message1",
      "webhookId": "a1d4b8a6-81f4-47c6-8bc8-702b3af73cf2",
      "credentials": {
        "telegramApi": {
          "id": "2v6xLPKkn3HD2Rdn",
          "name": "Telegram account 2"
        }
      }
    }
  ],
  "connections": {
    "Schedule Trigger": {
      "main": [
        [
          {
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP Request": {
      "main": [
        [
          {
            "node": "Code in JavaScript",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Code in JavaScript": {
      "main": [
        [
          {
            "node": "If",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If": {
      "main": [
        [
          {
            "node": "Send a text message",
            "type": "main",
            "index": 0
          }
        ],
        []
      ]
    },
    "Schedule Trigger1": {
      "main": [
        [
          {
            "node": "HTTP Request1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP Request1": {
      "main": [
        [
          {
            "node": "Code in JavaScript1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Code in JavaScript1": {
      "main": [
        [
          {
            "node": "Send a text message1",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "pinData": {
    "Schedule Trigger": [
      {
        "timestamp": "2026-04-29T07:24:03.152-04:00",
        "Readable date": "April 29th 2026, 7:24:03 am",
        "Readable time": "7:24:03 am",
        "Day of week": "Wednesday",
        "Year": "2026",
        "Month": "April",
        "Day of month": "29",
        "Hour": "07",
        "Minute": "24",
        "Second": "03",
        "Timezone": "Asia/Baku (UTC-04:00)"
      }
    ],
    "Schedule Trigger1": [
      {
        "timestamp": "2026-04-29T07:24:03.152-04:00",
        "Readable date": "April 29th 2026, 7:24:03 am",
        "Readable time": "7:24:03 am",
        "Day of week": "Wednesday",
        "Year": "2026",
        "Month": "April",
        "Day of month": "29",
        "Hour": "07",
        "Minute": "24",
        "Second": "03",
        "Timezone": "Asia/Baku (UTC-04:00)"
      }
    ]
  },
  "meta": {
    "templateCredsSetupCompleted": true,
    "instanceId": "8f42723d854102a22f8b6314b06bbb38f4b6e259798e3ba1bfd90033d4266ea4"
  }
}