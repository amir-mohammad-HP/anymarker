from rest_framework import serializers
from models import models, forms

class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Collection
        fields = '__all__'


class MarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Mark
        fields = '__all__'

class TemplateMarkBuilder:
    # template = serializers.SerializerMethodField('mark_template')
    form_class = None

    def mark_template(self, obj):
        if self.form_class :
            obj_ctx = self.model.objects.get(pk = obj.id).__dict__
            mark = models.Mark.objects.get(id = obj_ctx.get('mark_id'))

            if obj_ctx.get('url', None) :
                mark_field = {
                    'mark' : mark,
                    'url' : obj_ctx['url']}
            elif obj_ctx.get('image', None) :
                mark_field = {
                    'mark' : mark,
                    'url' : obj_ctx['image']}
            elif obj_ctx.get('note', None) :
                mark_field = {
                    'mark' : mark,
                    'url' : obj_ctx['note']}
            
            # build form and clear error messages
            form = self.form_class(mark_field)
            '''
            ['__class__', '__contains__', '__delattr__', 
            '__delitem__', '__dict__', '__dir__', '__doc__', 
            '__eq__', '__format__', '__ge__', '__getattribute__', 
            '__getitem__', '__gt__', '__hash__', '__html__', '__init__', 
            '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', 
            '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
            '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', 
            '__str__', '__subclasshook__', '__weakref__', 'as_data', 'as_json', 'as_text', 
            'as_ul', 'clear', 'copy', 'fromkeys', 'get', 'get_context', 'get_json_data', 'items', 
            'keys', 'pop', 'popitem', 'render', 'renderer', 'setdefault', 'template_name', 
            'template_name_text', 'template_name_ul', 'update', 'values']
            '''
            form.errors.clear()
            ctx = form.get_context()
            # ctx['fields'][0] ['__add__', '__class__', '__contains__', 
            # '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', 
            # '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', 
            # '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
            # '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
            # '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

            # ctx['fields'][0][0] = f"<div>{mark_field.get('mark').name}</div>" 
            print(ctx['fields'][0].count) 
            return form.as_p()
        return None

        


class URL_Serializer(TemplateMarkBuilder, serializers.ModelSerializer):
    template = serializers.SerializerMethodField('mark_template')
    form_class = forms.URLForm
    model = models.URL

    class Meta:
        model = models.URL
        fields = ['id', 'create_on', 'url', 'mark', 'template']
        # fields = '__all__'


class IMAGE_Serializer(TemplateMarkBuilder, serializers.ModelSerializer):
    template = serializers.SerializerMethodField('mark_template')
    form_class = forms.IMAGEForm
    model = models.IMAGE

    class Meta:
        model = models.IMAGE
        fields = '__all__'


class NOTE_Serializer(TemplateMarkBuilder, serializers.ModelSerializer):
    template = serializers.SerializerMethodField('mark_template')
    form_class = forms.NOTEForm
    model = models.NOTE

    class Meta:
        model = models.NOTE
        fields = '__all__'