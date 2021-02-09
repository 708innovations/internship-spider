from random import randint
from requests import post
from json import load

webhooks = load(open('config/config.json', 'r'))['webhooks']

def send(company: str, image: str, description: str, name: str, apply: str) -> bool:
    if not company or not apply:
        return False
    to_send = {
        'content': None,
        'embeds': [
            {
                'title': f'Now Hiring: {company}',
                'description': description,
                'url': apply,
                'color': randint(0, 0xFFFFFF),
                'fields': [
                    {
                        'name': f'Apply for {name}' if name else 'Apply Below',
                        'value': f'[Click here to submit an application]({apply})'
                    }
                ],
                'footer': {
                    'text': 'Powered by Gideon Tong\'s Internship Spider'
                },
                'thumbnail': {
                    'url': image if image else None
                }
            }
        ]
    }
    for hook in webhooks:
        response = post(hook, json=to_send)
        if response.status_code == 400:
            return False
    return True
