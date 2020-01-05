from django.conf import settings
from django.db import models
from imagekit.models import ProcessedImageField #이미지 처리하는 기능
from imagekit.processors import ResizeToFill #이미지사이즈 트리밍

# Create your models here.



def user_path(instance, filename): #instance - 사진
    from random import choice # 난수발생
    import string
    arr = [choice(string.ascii_letters) for _ in range(8)] #대소문자 구문없이 문자열을 가져온다.
    pid = '',join(arr)
    extension = filename.split('.')[-1] #확장자를 가져오겠다
    return 'accounts/{}/{}.{}'.format(instance.user.username, pid, extension) #어카운츠 아래에 폴더를 하나 만들어서 파일명을 저장하겠다.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE) #장고에서는 사용자를 나타내는 모델 제공
    
    nickname = models.CharField('별명',max_length=20, unique=True)
    
    picture = ProcessedImageField(upload_to=user_path,
                                 processors=[ResizeToFill(150,150)],
                                 format='JPEG',
                                 options={'quality': 90},
                                 blank=True,
                                 )
    
    
    about = models.CharField(max_length=300, blank=True) #할말이 많을수도 있고 없을수도 있고
    
    GENDER_C = (
        ('선택안함','선택안함'),
        ('여성','여성'),
        ('남성','남성'),
    )
    
    gender = models.CharField('성별(선택사항)',
                             max_length=10,
                             choices=GENDER_C,
                             default='N')
    
    def __str__(self):
        return self.nickname