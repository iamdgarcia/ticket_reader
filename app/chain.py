import requests
import json


def run_llm(api_key,base64_image):
    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }

    payload = {
    "model": "gpt-4o-mini",
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": """You will receive an image of a supermarket ticket. Your task is to extract the following details and return them in pure JSON format only. Ensure that no additional formatting like code blocks or markdown is included.

The JSON format should include:

supermarket_name: Name of the supermarket.
time_of_purchase: Time when the purchase was made.
product_list:
product_name: Name of each product.
product_qty: Quantity of the product purchased.
product_price: Price of a single unit of the product.
total_product_cost: Total cost of the product (qty x price).
product_category: The category to which the product belongs (e.g., groceries, electronics, etc.).
total_purchase_cost: The total amount spent on the entire purchase.
The output MUST be only the following JSON structure, fully populated with the extracted data:
json
```
{
  "supermarket_name": "string",
  "time_of_purchase": "HH:MM",
  "product_list": [
    {
      "product_name": "string",
      "product_qty": number,
      "product_price": number,
      "total_product_cost": number,
      "product_category": "string"
    }
  ],
  "total_purchase_cost": number
}```"""
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            }
        ]
        }
    ],
    "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    print(response.json()['choices'][0]['message']['content'])
    return json.loads(response.json()['choices'][0]['message']['content'].strip())

