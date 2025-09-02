import json
from channels.generic.websocket import AsyncWebsocketConsumer
from cargo.models import Cargo
from api.cargo_api.serializers import GetCargoSerializer
from asgiref.sync import sync_to_async


class ActiveCargosConsumer(AsyncWebsocketConsumer):
    group_name = "active_cargos"

    async def connect(self):
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()
        await self.send_active_cargos()


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("active_cargos", self.channel_name)


    @sync_to_async
    def get_active_cargos(self):
        cargos = Cargo.objects.filter(is_active=True).order_by('-created_at')
        return GetCargoSerializer(cargos, many=True).data


    async def send_active_cargos(self):
        data = await self.get_active_cargos()
        await self.send(text_data=json.dumps({"cargos": data}))


    async def receive(self, text_data):
        pass


    async def cargos_update(self, event):
        deleted_ids = event.get("deleted_ids")
        if deleted_ids:
            await self.send(text_data=json.dumps({
                "type": "delta",d
                "deleted_ids": deleted_ids
            }))
        await self.send_active_cargos()
