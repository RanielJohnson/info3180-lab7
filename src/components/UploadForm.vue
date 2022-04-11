<template>
    <form @submit.prevent= "uploadPhoto" method= "POST" id= "uploadForm" >       
        <div class="form-group">
            <label for="description">Description</label>
            <textarea class="form-control" id="description" rows="10" ></textarea>
        </div>  

        <div class="form-group">
            <label for="photo">Photo Upload</label>
            <input type="file" class="form-control-file" id="photo">
        </div>
    </form>
</template>

<script>
export default {
  data(){
      return {
        csrf_token: ''
      }
  },
  created(){
          this.getCsrfToken();
        },
  methods:{
       
      uploadPhoto(){
          let uploadForm = document.getElementById('uploadForm');
          let form_data = new FormData(uploadForm);
          fetch('/api/upload',{
              method: 'POST',
              body: form_data,
              headers: {
                    'X-CSRFToken': this.csrf_token
                    }
          })
          .then((response)=>{
              return response.json();
          })
          .then((data)=>{
              console.log(data);
          })
          .catch((error)=>{
              console.log(error);
          });
      },
      getCsrfToken(){
          let self =this;
          fetch('/api/csrf-token')
          .then(response=>
              response.json())          
          .then(data=>{
            self.csrf_token = data.csrf_token;
          })
      }
  },
};
</script>

<style>
</style>