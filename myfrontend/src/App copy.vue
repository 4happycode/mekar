<template>
  <div
    className="d-flex flex-column justify-content-center align-items-center mt-5"
  >
    <form @submit.prevent="handleSubmit">
      <div className="mb-3" v-for="resp in response" :key="resp.id">
        <label className="form-label text-capitalize">
          {{ resp.fieldName }}
        </label>
        <input
          :type="resp.type"
          v-model="formData[resp.fieldName]"
          className="form-control"
          required
        />
      </div>
      <button type="submit" className="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script>
import response from "./data.json";
export default {
  name: "App",
  components: {},
  data: () => ({
    response,
    formData: {},
  }),
  created: function () {
    this.response.map(
      (resp) =>
        (this.formData = { ...this.formData, [resp.fieldName]: resp.value })
    );
  },
  methods: {
    handleSubmit() {
      console.log(this.formData);
    },
  },
};
</script>

<style>
</style>
