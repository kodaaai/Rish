from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    """ ユーザーマネージャー """
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class university(models.Model):
    """ 大学名 """
    name = models.CharField('大学名', max_length=20, unique=True)

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    """ ユーザーカスタム """

    # 大学名
    university = models.ForeignKey(
        university,
        verbose_name='大学名',
        on_delete=models.CASCADE,
    )

    # 琉大メアド
    email = models.EmailField('琉大メールアドレス', unique=True)
    username = models.CharField('ユーザーネーム', max_length=20, default='user', unique=True)

    # 昼間主・夜間主
    openingSystems = (
        ('昼間主', '昼間主'),
        ('夜間主', '夜間主'),
    )
    openingSystem = models.CharField('昼間主・夜間主', choices=openingSystems, max_length=10)

    # 学部
    departments = (
        ('', '選択してください（必須）'),
        ('人文社会学部', '人文社会学部'),
        ('国際地域創造学部', '国際地域創造学部'),
        ('教育学部', '教育学部'),
        ('理学部', '理学部'),
        ('医学部', '医学部'),
        ('工学部', '工学部'),
        ('農学部', '農学部'),
    )
    department = models.CharField('学部', max_length=20, choices=departments)

    # 学科・専修
    subjects = (
        ('', '選択してください（必須）'),
        ('国際法政学科', '国際法政学科'),
        ('人間社会学科', '人間社会学科'),
        ('琉球アジア文化学科', '琉球アジア文化学科'),
        ('国際地域創造学科', '国際地域創造学科'),
        ('学校教育教員養成課程', '学校教育教員養成課程'),
        ('数理科学科', '数理科学科'),
        ('物質地球科学科', '物質地球科学科'),
        ('海洋自然科学科', '海洋自然科学科'),
        ('医学科', '医学科'),
        ('保健学科', '保健学科'),
        ('工学科', '工学科'),
        ('亜熱帯地域農学科', '亜熱帯地域農学科'),
        ('亜熱帯農林環境科学科', '亜熱帯農林環境科学科'),
        ('地域農業工学科', '地域農業工学科'),
        ('亜熱帯生物資源科学科', '亜熱帯生物資源科学科'),
    )
    subject = models.CharField('学科・課程', max_length=20, choices=subjects)

    # コース、プログラム
    courses = (
        ('', '選択してください（任意）'),
        ('法学プログラム', '法学プログラム'),
        ('政治・国際関係学プログラム', '政治・国際関係学プログラム'),
        ('哲学・教育学プログラム', '哲学・教育学プログラム'),
        ('心理学プログラム', '心理学プログラム'),
        ('社会学プログラム', '社会学プログラム'),
        ('歴史・民俗学プログラム', '歴史・民俗学プログラム'),
        ('言語学プログラム', '言語学プログラム'),
        ('文学プログラム', '文学プログラム'),
        ('観光地域デザインプログラム', '観光地域デザインプログラム'),
        ('経済学プログラム', '経済学プログラム'),
        ('地域文化科学プログラム', '地域文化科学プログラム'),
        ('国際言語文化プログラム', '国際言語文化プログラム'),
        ('経営プログラム', '経営プログラム'),
        ('小学校教育コース', '小学校教育コース'),
        ('中学校教育コース', '中学校教育コース'),
        ('特別支援教育コース', '特別支援教育コース'),
        ('物理系', '物理系'),
        ('地学系', '地学系'),
        ('化学系', '化学系'),
        ('生物系', '生物系'),
        ('機械工学コース', '機械工学コース'),
        ('エネルギー環境工学コース', 'エネルギー環境工学コース'),
        ('電気システム工学コース', '電気システム工学コース'),
        ('社会基盤デザインコース', '社会基盤デザインコース'),
        ('建築学コース', '建築学コース'),
        ('知能情報コース', '知能情報コース'),
        ('健康栄養科学コース', '健康栄養科学コース'),
    )
    course = models.CharField(
        'プログラム、コース',
        max_length=20,
        choices=courses,
        blank=True,
        null=True,
    )

    # 専攻
    majors = (
        ('', '選択してください（任意）'),
        ('学校教育専攻', '学校教育専攻'),
        ('教科教育専攻', '教科教育専攻'),
        ('哲学・教育学プログラム', '哲学・教育学プログラム'),
        ('特別支援教育専攻', '特別支援教育専攻'),
    )
    major = models.CharField('専攻', max_length=20, choices=majors, blank=True, null=True)

    # 専修
    specializations = (
        ('', '選択してください（任意）'),
        ('国語教育専修', '国語教育専修'),
        ('社会科教育専修', '社会科教育専修'),
        ('数学教育専修', '数学教育専修'),
        ('理科教育専修', '理科教育専修'),
        ('音楽教育専修', '音楽教育専修'),
        ('美術教育専修', '美術教育専修'),
        ('技術教育専修', '技術教育専修'),
        ('生活科学教育専修', '生活科学教育専修'),
        ('英語教育専修', '英語教育専修'),
        ('特別支援教育専修', '特別支援教育専修'),
    )
    specialization = models.CharField(
        '専修',
        max_length=20,
        choices=specializations,
        blank=True,
        null=True
    )

    # 卒業見込み
    graduationYears = (
        ('', '選択してください（必須）'),
        ('2022年', '2022年'),
        ('2023年', '2023年'),
        ('2024年', '2024年'),
        ('2025年', '2025年'),
    )

    # 卒業見込み
    graduationYear = models.CharField('卒業見込み年', choices=graduationYears, max_length=10)

    # 登録日
    created_at = models.DateField('登録日', auto_now_add=True)

    # 更新日
    updated_at = models.DateField('更新日', auto_now=True)

    # is_activeはBAN機能のようなもの。チェックを外すとそのユーザーはログインできない。
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['university', 'openingSystem',
                       'department', 'subject', 'graduationYear', 'username']

    def __str__(self):
        return self.email
