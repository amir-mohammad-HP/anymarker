from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, post_delete
from models.models import IMAGE, URL, NOTE
import os   
from django.conf import settings 
from django.core.exceptions import ValidationError

def model_checker(sender, instance, *args, **kwargs):
    print(instance.mark.model)
    print(instance.model)
    if instance.model[0] != instance.mark.model:
        raise ValidationError(f'your not allowed to add {instance.model[0]} instance to  {instance.mark.model} Mark model')
    pass

# PRE SAVE :
@receiver(pre_save, sender = IMAGE)
def Image_pre_save(sender, instance, *args, **kwargs):

    model_checker(sender, instance, *args, **kwargs)


@receiver(pre_save, sender = NOTE)
def Note_pre_save(sender, instance, *args, **kwargs):

    model_checker(sender, instance, *args, **kwargs)


@receiver(pre_save, sender = URL)
def URL_pre_save(sender, instance, *args, **kwargs):

    model_checker(sender, instance, *args, **kwargs)



# POST DELETE :
@receiver(post_delete, sender = IMAGE)
def Image_post_delete(sender, instance, *args, **kwargs):
    
    file_path = f'{settings.MEDIA_ROOT}/{instance}'

    if os.path.isfile(file_path):
       os.remove(file_path)

    # delete empty directory :
    search_directory = True
    directory = file_path
    while search_directory:
        splited_directory = directory.split('/')[:-1]
        if 'user_' in splited_directory[-1] :
            search_directory = True
            break

        directory = "/".join(splited_directory)
        print(directory)

        if len(os.listdir(directory)) == 0:
            try:
                os.d=os.rmdir(directory)
            except:
                search_directory = False
        else:
            search_directory = False


