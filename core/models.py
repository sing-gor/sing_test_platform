from django.db import models
PYTESTCASE_CATEGORY = (
    ('api', "API 接口测试"),
    ('business', "业务流程测试")
)

API_PLATFORM = (
    ('aliyun', '阿里云原生'),
    ('processing', '二次加工'),
    ('case', '用例'),
    ('doc', '文档示例'),
)
AUTO_FLOW_STATUS = (
    ('0', '下架'),
    ('1', '上架'),
)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.
class ApiDataModelV2(BaseModel):
    slug = models.SlugField(verbose_name="api_id", max_length=64, unique=True)
    title = models.CharField(verbose_name="标题", max_length=64)
    alias = models.CharField(verbose_name="别名标题", max_length=64, blank=True, null=True)
    description = models.TextField(verbose_name="描述", blank=True, null=True)
    platform = models.CharField(verbose_name="分类", choices=API_PLATFORM, max_length=64)
    path = models.CharField(verbose_name='path', max_length=512)
    request_method = models.CharField(verbose_name='method', max_length=12)
    mock = models.IntegerField(verbose_name='Mock', default=0, help_text='是否开启Mock')
    need_sign = models.IntegerField(verbose_name='验签', default=0, help_text='是否需要橡树加签')
    group_slug = models.CharField(verbose_name="分组索引", max_length=64)
    group_title = models.CharField(verbose_name="分组标题", max_length=64)
    root_slug = models.CharField(verbose_name="root slug", max_length=64, null=True, blank=True)
    parent_slug = models.CharField(verbose_name="父级slug", max_length=64, null=True, blank=True)
    weight = models.IntegerField(verbose_name='权重', default=0)
    payload = models.JSONField(verbose_name='提交参数集', default=list)
    assert_body = models.JSONField(verbose_name='断言参数集', default=list)
    status = models.CharField(verbose_name='是否运行', default='1', choices=AUTO_FLOW_STATUS, max_length=4,
                              help_text='是否执行，不为0 则进行')

    class Meta:
        db_table = "api_data"
        verbose_name = 'Api数据集'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ApiEnvironment(models.Model):
    title = models.CharField(verbose_name="标题", max_length=64)
    slug = models.SlugField(verbose_name="api_id", max_length=64, unique=True)
    description = models.TextField(verbose_name="描述", blank=True, null=True)
    host = models.CharField(verbose_name="域名", max_length=128)
    api_env = models.CharField(verbose_name='api环境', max_length=24)
    api_app_key = models.CharField(verbose_name='网关key', max_length=64)
    api_app_secret = models.CharField(verbose_name='网关密码', max_length=64)
    private_key = models.TextField(verbose_name='私钥')
    agent_id = models.CharField(verbose_name='agent_id', max_length=64)
    namespace = models.CharField(verbose_name='namespace', max_length=64)

    class Meta:
        db_table = "api_environment"
        verbose_name = 'api环境'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ApiEnvironmentEnemy(models.Model):
    title = models.CharField(verbose_name="标题", max_length=64)
    value = models.TextField(verbose_name="参数")
    description = models.TextField(verbose_name="描述", blank=True, null=True)
    slug = models.SlugField(verbose_name="api_id", max_length=64)

    class Meta:
        db_table = "api_environment_enemy"
        verbose_name = 'api环境元素'
        verbose_name_plural = verbose_name
        unique_together = ('title', 'slug')

    def __str__(self):
        return self.title


class ApiCase(BaseModel):
    slug = models.SlugField(verbose_name="case_id", max_length=64, unique=True)
    title = models.CharField(verbose_name="标题", max_length=64)
    description = models.TextField(verbose_name="描述", blank=True, null=True)

    class Meta:
        db_table = "api_case"
        verbose_name = '接口用例'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.slug}-{self.title}'


class CaseApiRelationshipV2(BaseModel):
    """
    允许重复 绑定 一般不会出现
    """
    case_slug = models.CharField(verbose_name="case唯一索引", max_length=64)
    api_slug = models.CharField(verbose_name="api唯一索引", max_length=64)
    status = models.CharField(verbose_name='是否运行', default='0', choices=AUTO_FLOW_STATUS, max_length=4,
                              help_text='是否执行，不为0 则进行')

    class Meta:
        db_table = "case_api_relationship"
        verbose_name = '用例接口关联关系'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.case_slug}-{self.api_slug}'
