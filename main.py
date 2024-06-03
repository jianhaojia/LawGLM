
import json

from langchain_openai import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from openai import OpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_core.output_parsers import StrOutputParser
from langchain.output_parsers import JsonOutputToolsParser
from langchain_core.tools import tool
from zhipuai import ZhipuAI

llm = ChatOpenAI(
    temperature=0.95,
    model="glm-4",
    openai_api_key="bfc9a09dce86070855c637f889604bc8.eFiLKw1ZcQ91pqtn",
    openai_api_base="https://open.bigmodel.cn/api/paas/v4/"
)
from baseUrl.base import get_company_name,get_company_info,search_company_name_by_register,get_company_register,search_company_name_by_sub_info,get_sub_company_info,search_case_num_by_legal_document,get_legal_document

client = ZhipuAI(api_key="bfc9a09dce86070855c637f889604bc8.eFiLKw1ZcQ91pqtn")
messages = []
tools=[{
            "type": "function",
            "function": {
                "name": "get_company_info",
                "description": "用户希望通过这个方法来获得公司基本信息，需要提供公司名字",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "company_name": {
                            "type": "string",
                            "description":"公司名字"
                        }
                    }
                },
                "required": ["company_name"],
            }
        },
            {
                "type": "function",
                "function": {
                    "name": "get_company_name",
                    "description": """根据传入的key，value获取公司的名称，user的内容必须包含公司内容的属性名和对应值，且仅仅有获取公司名字的表达，如果是传入公司名字的key，value则不是这个方法""",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "key": {
                                "type": "string",
                                "description":"是属性的名称,必须是中文"
                            },
                            "value": {
                                "type": "string",
                                "description": "是属性的值"
                            }
                        },
                        "required": ["key","value"]
                    }
                }
            },
{
            "type": "function",
            "function": {
                "name": "get_company_register",
                "description": "用户希望用这个方法来获取公司注册信息，问题需要有注册等类似的词语，且提供公司名字",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "company_name": {
                            "type": "string",
                            "description":"公司名字"
                        }
                    }
                },
                "required": ["company_name"],
            }
        },
            {
                "type": "function",
                "function": {
                    "name": "search_company_name_by_register",
                    "description": """在注册公司信息里面，根据传入的key，value获取公司的名称，user的内容必须包含公司内容的属性名和对应值，且仅仅有获取公司名字的表达，如果是传入公司名字的key，value则不是这个方法""",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "key": {
                                "type": "string",
                                "description":"是属性的名称,必须是中文"
                            },
                            "value": {
                                "type": "string",
                                "description": "是属性的值"
                            }
                        },
                        "required": ["key","value"]
                    }
                }
            },
{
            "type": "function",
            "function": {
                "name": "get_sub_company_info",
                "description": "关于关联公司的信息，根据公司名字获取关联公司的全部基本信息，user的内容必须包含公司名称，且有获取公司信息的表达",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "company_name": {
                            "type": "string",
                            "description":"公司名字"
                        }
                    }
                },
                "required": ["company_name"],
            }
        },
            {
                "type": "function",
                "function": {
                    "name": "search_company_name_by_sub_info",
                    "description": """关于关联公司的信息，根据传入的key，value获取关联公司的名称，user的内容必须包含公司内容的属性名和对应值，且仅仅有获取公司名字的表达，如果是传入公司名字的key，value则不是这个方法""",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "key": {
                                "type": "string",
                                "description":"是属性的名称,必须是中文"
                            },
                            "value": {
                                "type": "string",
                                "description": "是属性的值"
                            }
                        },
                        "required": ["key","value"]
                    }
                }
            },
{
            "type": "function",
            "function": {
                "name": "get_legal_document",
                "description": "根据案号获得该案所有基本信息，如何解析到的case_num没有号结尾，则加个号",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "case_num": {
                            "type": "string",
                            "description":"案号"
                        }
                    }
                },
                "required": ["case_num"],
            }
        },
            {
                "type": "function",
                "function": {
                    "name": "search_case_num_by_legal_document",
                    "description": """根据法律文书某个字段是某个值来查询具体的案号""",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "key": {
                                "type": "string",
                                "description":"是属性的名称,必须是中文，不能是案件号"
                            },
                            "value": {
                                "type": "string",
                                "description": "是属性的值"
                            }
                        },
                        "required": ["key","value"]
                    }
                }
            }
        ]
def get_completion(messages):
    response = client.chat.completions.create(
        model="glm-4",
        messages=messages,
        temperature=0.7,
        tools=tools
    )
    return response.choices[0].message



def print_json(data):
    """
    打印参数。如果参数是有结构的（如字典或列表），则以格式化的 JSON 形式打印；
    否则，直接打印该值。
    """
    if hasattr(data, 'model_dump_json'):
        data = json.loads(data.model_dump_json())

    if (isinstance(data, (list))):
        for item in data:
            print_json(item)
    elif (isinstance(data, (dict))):
        print(json.dumps(
            data,
            indent=4,
            ensure_ascii=False
        ))
    else:
        print(data)



def parse_function_call(model_response,messages):
    if model_response.choices[0].message.tool_calls:
        tool_call = model_response.choices[0].message.tool_calls[0]
        args = tool_call.function.arguments
        function_result = {}
        if tool_call.function.name == "get_company_name":
            function_result = get_company_name(**json.loads(args))
        if tool_call.function.name == "get_company_info":
            function_result = get_company_info(**json.loads(args))
        if tool_call.function.name == "get_company_register":
            function_result = get_company_register(**json.loads(args))
        if tool_call.function.name == "search_company_name_by_register":
            function_result = search_company_name_by_register(**json.loads(args))
        if tool_call.function.name == "get_sub_company_info":
            function_result = get_sub_company_info(**json.loads(args))
        if tool_call.function.name == "search_company_name_by_sub_info":
            function_result = search_company_name_by_sub_info(**json.loads(args))
        if tool_call.function.name == "search_case_num_by_legal_document":
            function_result = search_case_num_by_legal_document(**json.loads(args))
        if tool_call.function.name == "get_legal_document":
            function_result = get_legal_document(**json.loads(args))
        messages.append({
            "role": "tool",
            "content": f"{json.dumps(function_result)}",
            "tool_call_id":tool_call.id
        })
        response = client.chat.completions.create(
            model="glm-4",
            messages=messages,
            tools=tools,
        )
        print(messages)
        print(response.choices[0].message.content)
        messages.append(response.choices[0].message.model_dump())




prompt = "深圳能源集团股份有限公司为被告的次数是多少次"


messages.append({"role": "system", "content": "不要假设或猜测传入函数的参数值。如果用户的描述不明确，请要求用户提供必要信息"})
messages.append({"role": "user", "content": prompt})
# llm.invoke("请")

response = client.chat.completions.create(
    model="glm-4",  # 填写需要调用的模型名称
    messages=messages,
    tools=tools,
)
print(response.choices[0].message)
messages.append(response.choices[0].message.model_dump())

parse_function_call(response, messages)
parse_function_call(response, messages)



