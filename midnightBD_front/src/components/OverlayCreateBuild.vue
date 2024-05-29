<template>
  <Dialog modal header="Новый Заказ" :style="{ width: '30rem' }">
    <div class="input-container">
      <inputInfo
        @updateInput="inputClientID = $event"
        :iconClass="'pi pi-user'"
        :placeholder="'Клиент'"
      />

      <div class="gpu-input-container">
        <Dropdown
          v-model="inputGPUBrand"
          :options="possibleGPUBrands"
          optionLabel="name"
          placeholder="Компания"
        />
        <AutoComplete
          v-model="inputGPUModel"
          :suggestions="autocompleteTemp"
          @complete="searchGPU"
        />
      </div>

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
    </div>
    <Button label="Добавить сборку" @click="addOrder()" />
  </Dialog>
</template>

<script>
import Dialog from "primevue/dialog";
import inputInfo from "./inputInfo.vue";
import Button from "primevue/button";
import AutoComplete from "primevue/autocomplete";
import Dropdown from "primevue/dropdown";

export default {
  name: "OverlayCreateBuild",
  components: {
    Dialog,
    inputInfo,
    Button,
    AutoComplete,
    Dropdown,
  },
  data() {
    return {
      inputClientID: "",
      inputCPU: "",
      inputGPUBrand: "",
      inputGPUModel: "",
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

      possibleGPUBrands: [
        { name: "AMD", code: "amd" },
        { name: "Nvidia", code: "nvidia" },
      ],

      autocompleteTemp: [],
      autocompleteGPU: [],
    };
  },
  mounted() {
    console.log("AAAAAAAAAA");
    console.log(this.autocompleteGPU);
  },
  methods: {
    addOrder() {
      fetch("http://127.0.0.1:7900/tables/orders_build/rows", {
        method: "POST",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify({
          row: [
            this.inputClientID,
            this.inputCPU,
            `${this.inputGPUBrand} ${this.inputGPUModel}`,
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
    getAutoComplete(component, brand) {
      fetch(`http://127.0.0.1:7900/known/${component}/${brand}`)
        .then((response) => response.json())
        .then((data) => {
          console.log(data.data);
          this.autocompleteGPU = data.data;
        })
        .catch((error) => {
          console.error("Error fetching autocomplete data:", error);
        });
    },

    searchGPU(event) {
      console.log(this.autocompleteGPU);
      if (!event.query.trim().length) {
        this.autocompleteTemp = [...this.autocompleteGPU];
      } else {
        this.autocompleteTemp = this.autocompleteGPU.filter((gpu) => {
          return gpu.toLowerCase().includes(event.query.toLowerCase());
        });
      }
    },
  },
  watch: {
    inputGPUBrand(selected, _) {
      console.log(selected);
      if (selected.code == "amd") {
        this.getAutoComplete("gpu", "amd");
      } else if (selected.code == "nvidia") {
        this.getAutoComplete("gpu", "nvidia");
      }
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
