<template>
  <Dialog modal header="Новый Заказ" :style="{ width: '30rem' }">
    <inputInfo
      @updateInput="inputClientID = $event"
      :iconClass="'pi pi-user'"
      :placeholder="'Клиент'"
    />
    <inputInfo
      @updateInput="inputGPU = $event"
      :iconClass="'pi pi-user'"
      :placeholder="'Видеокарта'"
    />
    <inputInfo
      @updateInput="inputMotherboard = $event"
      :iconClass="'pi pi-user'"
      :placeholder="'Материнская плата'"
    />
    <inputInfo
      @updateInput="inputRAM = $event"
      :iconClass="'pi pi-user'"
      :placeholder="'Оперативная память'"
    />
    <inputInfo
      @updateInput="inputPSU = $event"
      :iconClass="'pi pi-user'"
      :placeholder="'Блок Питания'"
    />
    <inputInfo
      @updateInput="inputHDDSSD = $event"
      :iconClass="'pi pi-user'"
      :placeholder="'Диски'"
    />
    <inputInfo
      @updateInput="inputCase = $event"
      :iconClass="'pi pi-user'"
      :placeholder="'Корпус'"
    />
    <inputInfo
      @updateInput="inputCooler = $event"
      :iconClass="'pi pi-user'"
      :placeholder="'Кулер'"
    />
    <inputInfo
      @updateInput="inputFans = $event"
      :iconClass="'pi pi-user'"
      :placeholder="'Вертушки'"
    />
    <inputInfo
      @updateInput="inputEntry = $event"
      :iconClass="'pi pi-user'"
      :placeholder="'Дата Приема'"
    />
    <inputInfo
      @updateInput="inputFinish = $event"
      :iconClass="'pi pi-user'"
      :placeholder="'Дата Конца'"
    />
    <inputInfo
      @updateInput="inputPrice = $event"
      :iconClass="'pi pi-user'"
      :placeholder="'Цена'"
    />
    <inputInfo
      @updateInput="inputStatus = $event"
      :iconClass="'pi pi-user'"
      :placeholder="'Статус'"
    />

    <Button label="Добавить сборку" @click="addOrder()" />
  </Dialog>
</template>

<script>
import Dialog from "primevue/dialog";
import inputInfo from "./inputInfo.vue";
import Button from "primevue/button";

export default {
  name: "OverlayCreateBuild",
  components: {
    Dialog,
    inputInfo,
    Button,
  },
  data() {
    return {
      inputClientID: "",
      inputCPU: "",
      inputGPU: "",
      inputMotherboard: "",
      inputRAM: "",
      inputPSU: "",
      inputHDDSSD: "",
      inputCase: "",
      inputCooler: "",
      inputFans: "",
      inputEntry: "",
      inputFinish: "",
      inputPrice: "",
      inputStatus: "",
    };
  },
  methods: {
    addOrder() {
      fetch("http://127.0.0.1:7900/orders_build/rows", {
        method: "POST",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify({
          row: [
            this.inputClientID,
            this.inputCPU,
            this.inputGPU,
            this.inputMotherboard,
            this.inputRAM,
            this.inputPSU,
            this.inputHDDSSD,
            this.inputCase,
            this.inputCooler,
            this.inputFans,
            this.inputEntry,
            this.inputFinish,
            this.inputPrice,
            this.inputStatus,
          ],
        }),
      })
        .then((response) => response.json())
        .then((json) => console.log(json))
        .then(() => window.location.reload());
      console.log("adding client");
    },
  },
};
</script>

<style>
p-icon-field,
p-button {
  margin: 10rem;
}
</style>
