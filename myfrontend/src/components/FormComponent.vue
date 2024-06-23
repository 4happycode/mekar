<template>
    <div class="form-container">
      <form @submit.prevent="submitForm" class="form">
        <div class="form-group">
          <label for="name">Name:</label>
          <input type="text" id="name" v-model="formData.name" class="form-control" required>
        </div>
        <div class="form-group">
          <label for="identityNumber">Identity Number:</label>
          <input type="text" id="identityNumber" v-model="formData.identityNumber" class="form-control" required>
        </div>
        <div class="form-group">
          <label for="email">Email Address:</label>
          <input type="email" id="email" v-model="formData.email" class="form-control" required>
          <span v-if="formError.email" class="error-msg">{{ formError.email }}</span>
        </div>
        <div class="form-group">
          <label for="dob">Date of Birth:</label>
          <input type="date" id="dob" v-model="formData.dateOfBirth" class="form-control" required>
        </div>
        <button type="submit" class="btn-submit">Submit</button>
        <p v-if="formError.other" class="error-msg">{{ formError.other }}</p>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        formData: {
          name: '',
          identityNumber: '',
          email: '',
          dateOfBirth: ''
        },
        formError: {}
      };
    },
    methods: {
      async submitForm() {
        // Validate form fields
        if (!this.validateForm()) {
          return;
        }
        try {
          // Assuming you have axios or fetch configured
          const response = await fetch(`${process.env.VUE_APP_Backend_URL}create`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(this.formData)
          });
  
          if (!response.ok) {
            const errorMessage = await response.json();
            throw new Error(errorMessage.detail);
          }
  
          // Reset form after successful submission
          this.formData.name = '';
          this.formData.identityNumber = '';
          this.formData.email = '';
          this.formData.dateOfBirth = '';
  
          alert('Form submitted successfully!');
        } catch (error) {
          console.error('Error submitting form:', error);
          this.formError.other = error.message || 'Terjadi kesalahan. Silakan coba lagi.';
        }
      },
      validateForm() {
        // Reset form error messages
        this.formError = {};
  
        // Basic validation
        if (!this.formData.name || !this.formData.identityNumber || !this.formData.email || !this.formData.dateOfBirth) {
          this.formError.other = 'Please fill in all fields.';
          return false;
        }
  
        // Email validation with regex
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(this.formData.email)) {
          this.formError.email = 'Invalid email address.';
          return false;
        }
  
        // Additional validation logic can be added here
  
        return true;
      }
    }
  };
  </script>
  