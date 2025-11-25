from django.db import models

class Term(models.Model):
    word = models.CharField(max_length=200, verbose_name="Термин")
    definition = models.TextField(verbose_name="Определение")
    image_upload = models.ImageField(upload_to='uploads/images/', blank=True, null=True, verbose_name="Загрузить изображение")
    video_upload = models.FileField(upload_to='uploads/videos/', blank=True, null=True, verbose_name="Загрузить видео")
    image_path = models.CharField(max_length=500, blank=True, null=True, verbose_name="Путь к изображению в static")
    video_path = models.CharField(max_length=500, blank=True, null=True, verbose_name="Путь к видео в static")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")  # ← Добавьте это поле

    def save(self, *args, **kwargs):
        # Если загружено изображение
        if self.image_upload:
            # Копируем файл в static/images/
            filename = self.image_upload.name
            import os
            from django.conf import settings
            filepath = os.path.join(settings.STATICFILES_DIRS[0], 'images', filename)
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, 'wb') as f:
                f.write(self.image_upload.read())
            self.image_path = filename
            self.image_upload = None  # Не сохраняем в uploads

        # Если загружено видео
        if self.video_upload:
            # Копируем файл в static/videos/
            filename = self.video_upload.name
            filepath = os.path.join(settings.STATICFILES_DIRS[0], 'videos', filename)
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, 'wb') as f:
                f.write(self.video_upload.read())
            self.video_path = filename
            self.video_upload = None  # Не сохраняем в uploads

        super().save(*args, **kwargs)

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = "Термин"
        verbose_name_plural = "Термины"