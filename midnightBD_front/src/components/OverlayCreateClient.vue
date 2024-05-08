<template>
    <Dialog modal header="Новый Клиент" :style="{ width: '30rem'}">
        <inputInfo @updateInput="inputName     = $event" :iconClass="'pi pi-user'"     :placeholder="'Имя'" /> 
        <inputInfo @updateInput="inputPhone    = $event" :iconClass="'pi pi-phone'"    :placeholder="'Телефон'" /> 
        <inputInfo @updateInput="inputTelegram = $event" :iconClass="'pi pi-telegram'" :placeholder="'Телеграм'" /> 
        <inputInfo @updateInput="inputVK       = $event" :iconClass="'pi pi-mobile'"   :placeholder="'ВК'" /> 
        <inputInfo @updateInput="inputAvito    = $event" :iconClass="'pi pi-inbox'"    :placeholder="'Авито'" /> 
        <inputInfo @updateInput="inputWhatsapp = $event" :iconClass="'pi pi-whatsapp'" :placeholder="'Whatsapp'" /> 

        <Button label="Добавить клиента" @click="addClient()" />

    </Dialog>
</template>

<script>
import Dialog from 'primevue/dialog'
import inputInfo from './inputInfo.vue'
import Button from 'primevue/button'


export default {
    name: "OverlayCreateClient",
    components: {
        Dialog,
        inputInfo,
        Button
    },
    data() {
        return {
            inputName: "",
            inputPhone: "",
            inputTelegram: "",
            inputVK: "",
            inputAvito: "",
            inputWhatsapp: "",
        }
    },
    methods : {
        addClient() {
            fetch("http://127.0.0.1:7900/clients/rows", {
                method: "POST",
                headers: {
                    "Content-type": "application/json",
                },
                body: JSON.stringify({
                    row: [this.inputName, this.inputPhone, this.inputTelegram, this.inputVK, this.inputAvito, this.inputWhatsapp]
                })
            })
            .then((response) => response.json())
            .then((json) => console.log(json))
            .then(() => window.location.reload())
            console.log("adding client")

        }
    }
}

</script>

<style>
p-icon-field, p-button {
    margin: 10rem;
}
</style>
