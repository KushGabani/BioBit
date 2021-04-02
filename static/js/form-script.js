$(document).ready(function () {
  console.log("ready!");
  $(".image-section").hide();

  function readURL(input) {
    if (input.files && input.files[0]) {
      var reader = new FileReader();
      reader.onload = function (e) {
        $("#imagePreview").css(
          "background-image",
          "url(" + e.target.result + ")"
        );
        $("#imagePreview").hide();
        $("#imagePreview").fadeIn(650);
      };
      reader.readAsDataURL(input.files[0]);
    }
  }

  $("#image-upload").change(function () {
    $(".image-section").show();
    readURL(this);
  });
});
