from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import BookReservation, BookInstance, BookRental


@receiver(post_save, sender=BookRental)
def update_bookinstance_status(sender, instance, created, **kwargs):
    if created:
        book = BookInstance.objects.get(pk=instance.book.id)
        book.status = "O"
        book.save()
        bookReservation = BookReservation.objects.get(book=instance.book.id)
        if bookReservation:
            bookReservation.delete()

@receiver(post_delete, sender=BookRental)
def update_bookinstance_status_delete(sender, instance, **kwargs):        
        book = BookInstance.objects.get(pk=instance.book.id)
        book.status = "A"
        book.save()

@receiver(post_delete, sender=BookReservation)
def update_bookinstance_status_delete(sender, instance, **kwargs):        
        book = BookInstance.objects.get(pk=instance.book.id)
        book.status = "A"
        book.save()