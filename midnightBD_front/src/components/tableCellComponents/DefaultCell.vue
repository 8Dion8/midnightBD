<template>
    <p>{{ rowData[rowIndexToGet] }}</p>
</template>

<script>
export default {
    name: "DefaultCell",
    props: ['rowData', 'rowIndexToGet'],
    mounted() {
        console.log(this.rowData)
        console.log(this.rowIndexToGet)
    }
}

</script>
