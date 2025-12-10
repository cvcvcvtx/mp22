from .models import ActionLog

class ActionLogMixin:
    """
    Миксин, который автоматически пишет логи при создании, обновлении и удалении.
    """

    def _log_action(self, action_type, instance):
        """метод для записи лога"""
        user = self.request.user if self.request.user.is_authenticated else None
        
        
        record_info = str(instance)
        #  "Contact: Иван Иванов"
        record_info = f"{instance._meta.verbose_name}: {record_info}"

        ActionLog.objects.create(
            user=user,
            action_type=action_type,
            record_info=record_info[:255] 
        )

    def perform_create(self, serializer):
        
        instance = serializer.save() 
        self._log_action(ActionLog.ActionType.CREATED, instance) 

    def perform_update(self, serializer):
        
        instance = serializer.save()
        self._log_action(ActionLog.ActionType.UPDATED, instance)

    def perform_destroy(self, instance):
        
        
        self._log_action(ActionLog.ActionType.DELETED, instance)
        instance.delete()