import json

class CompanyInfo:
    def __init__(self, 公司名称, 公司简称=None, 英文名称=None, 关联证券=None, 公司代码=None, 曾用简称=None, 所属市场=None, 所属行业=None, 上市日期=None, 法人代表=None, 总经理=None, 董秘=None, 邮政编码=None, 注册地址=None, 办公地址=None, 联系电话=None, 传真=None, 官方网址=None, 电子邮箱=None, 入选指数=None, 主营业务=None, 经营范围=None, 机构简介=None, 每股面值=None, 首发价格=None, 首发募资净额=None, 首发主承销商=None):
        self.公司名称 = 公司名称
        self.公司简称 = 公司简称
        self.英文名称 = 英文名称
        self.关联证券 = 关联证券
        self.公司代码 = 公司代码
        self.曾用简称 = 曾用简称
        self.所属市场 = 所属市场
        self.所属行业 = 所属行业
        self.上市日期 = 上市日期
        self.法人代表 = 法人代表
        self.总经理 = 总经理
        self.董秘 = 董秘
        self.邮政编码 = 邮政编码
        self.注册地址 = 注册地址
        self.办公地址 = 办公地址
        self.联系电话 = 联系电话
        self.传真 = 传真
        self.官方网站 = 官方网址
        self.电子邮箱 = 电子邮箱
        self.入选指数 = 入选指数
        self.主营业务 = 主营业务
        self.经营范围 = 经营范围
        self.机构简介 = 机构简介
        self.每股面值 = 每股面值
        self.首发价格 = 首发价格
        self.首发募资净额 = 首发募资净额
        self.首发主承销商 = 首发主承销商

# 假数据
json_list = [
    """{"公司名称": "广州发展集团股份有限公司", "公司简称": "广州发展", "英文名称": "Guangzhou Development Group Inc.", "关联证券": "600098", "公司代码": "600098", "曾用简称": "广州发展实业控股集团股份有限公司", "所属市场": "上交所", "所属行业": "能源", "上市日期": "1992-11-13", "法人代表": "李明", "总经理": "张三", "董秘": "李四", "邮政编码": "510620", "注册地址": "广州市天河区珠江新城", "办公地址": "广州市天河区珠江新城", "联系电话": "020-12345678", "传真": "020-87654321", "官方网站": "www.gzdevelopment.com", "电子邮箱": "info@gzdevelopment.com", "入选指数": "上证50", "主营业务": "能源开发", "经营范围": "能源投资,开发,建设,经营", "机构简介": "广州发展集团股份有限公司是一家专业从事能源投资的公司", "每股面值": "1元", "首发价格": "3元", "首发募资净额": "1亿元", "首发主承销商": "中信证券"}""",
    """{"公司名称": "广州发展集团股份有限公司1", "公司简称": "广州发展1", "英文名称": "Guangzhou Development Group Inc.1", "关联证券": "600099", "公司代码": "600099", "曾用简称": "广州发展实业控股集团股份有限公司1", "所属市场": "深交所", "所属行业": "环保", "上市日期": "1993-12-14", "法人代表": "王五", "总经理": "赵六", "董秘": "孙七", "邮政编码": "510621", "注册地址": "广州市天河区天河北路", "办公地址": "广州市天河区天河北路", "联系电话": "020-87654322", "传真": "020-87654323", "官方网站": "www.gzdevelopment1.com", "电子邮箱": "info@gzdevelopment1.com", "入选指数": "深证100", "主营业务": "环保项目", "经营范围": "环保投资,开发,建设,经营", "机构简介": "广州发展集团股份有限公司1是一家专业从事环保投资的公司", "每股面值": "2元", "首发价格": "4元", "首发募资净额": "2亿元", "首发主承销商": "国泰君安"}"""
]

# get_company_info 方法
def get_company_info(company_name: str) -> CompanyInfo:
    for json_str in json_list:
        company_data = json.loads(json_str)
        if company_data.get("公司名称") == company_name:
            return CompanyInfo(
                公司名称=company_data.get("公司名称"),
                公司简称=company_data.get("公司简称"),
                英文名称=company_data.get("英文名称"),
                关联证券=company_data.get("关联证券"),
                公司代码=company_data.get("公司代码"),
                曾用简称=company_data.get("曾用简称"),
                所属市场=company_data.get("所属市场"),
                所属行业=company_data.get("所属行业"),
                上市日期=company_data.get("上市日期"),
                法人代表=company_data.get("法人代表"),
                总经理=company_data.get("总经理"),
                董秘=company_data.get("董秘"),
                邮政编码=company_data.get("邮政编码"),
                注册地址=company_data.get("注册地址"),
                办公地址=company_data.get("办公地址"),
                联系电话=company_data.get("联系电话"),
                传真=company_data.get("传真"),
                官方网站=company_data.get("官方网站"),
                电子邮箱=company_data.get("电子邮箱"),
                入选指数=company_data.get("入选指数"),
                主营业务=company_data.get("主营业务"),
                经营范围=company_data.get("经营范围"),
                机构简介=company_data.get("机构简介"),
                每股面值=company_data.get("每股面值"),
                首发价格=company_data.get("首发价格"),
                首发募资净额=company_data.get("首发募资净额"),
                首发主承销商=company_data.get("首发主承销商")
            )
    return None

# search_company_name_by_info 方法
def search_company_name_by_info(key: str, value: str) -> str:
    for json_str in json_list:
        company_data = json.loads(json_str)
        if company_data.get(key) == value:
            return company_data.get("公司名称")
    return None

# 测试
company_name = "广州发展集团股份有限公司"
company_info = get_company_info(company_name)
print(company_info.__dict__ if company_info else "公司信息未找到")

key = "公司简称"
value = "广州发展"
company_name = search_company_name_by_info(key, value)
print(company_name if company_name else "公司名称未找到")
