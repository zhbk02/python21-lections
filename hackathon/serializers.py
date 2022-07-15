from .models import *
class BaseSerializer:
    class Meta:
        fields = []
        queryset = []
    
    def serialize_obj(self, obj):
        fields = self.Meta.fields
        dict_ = {}
        for field in fields:
            dict_[field] = getattr(obj, field)
        return dict_
    
    def serialize_queryset(self, queryset=None):
        if queryset is None:
            queryset = self.Meta.queryset

        list_ = []
        for obj in queryset:
            dict_ = self.serialize_obj(obj)
            list_.append(dict_)
        return list_
class CarSerializer(BaseSerializer):
    class Meta:
        fields = ["mark", "model", "year", "eng", "color", "kuzov", "probeg", "price", "comments"]
        queryset = Car.objects
    
    def serialize_obj(self, obj):
        dict_ = super().serialize_obj(obj)
        dict_["comments"] = CommentSerializer().serialize_queryset(obj.comments)
        return dict_

class CommentSerializer(BaseSerializer):
    class Meta:
        fields = ["body"]
        queryset = Comment.objects

def obj_404(model, attr, val):
    found = False

    for obj in model.objects:
        obj_val = getattr(obj, attr)
        if obj_val == val:
            found = True
            break

    if not found:
        raise Exception(f"404 {model.__name__}  Not Found")
    
    return obj