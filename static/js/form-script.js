$(document).ready(function () {
  console.log("ready!");
  $(".image-section").hide();
  $("#result").hide();
  $(".predict").hide();

  //   function readURL(input) {
  //     if (input.files && input.files[0]) {
  //       var reader = new FileReader();
  //       reader.onload = function (e) {
  //         $("#imagePreview").css(
  //           "background-image",
  //           "url(" + e.target.result + ")"
  //         );
  //         $("#imagePreview").hide();
  //         $("#imagePreview").fadeIn(650);
  //       };
  //       reader.readAsDataURL(input.files[0]);
  //     }
  //   }

  //   $("#image-upload").change(function () {
  //     $(".image-section").show();
  //     $(".uploadBtn").hide();
  //     $(".predict").show();
  //     $("#result").text("");
  //     $("#result").hide();
  //     readURL(this);
  //   });

  $("#btn-predict").click(function () {
    var form_data = new FormData($("#uploadForm")[0]);
    $(this).hide();
    console.log("Reached ajax post. ");
    $.ajax({
      type: "POST",
      url: window.location.origin + "/predict",
      data: form_data,
      contentType: false,
      cache: false,
      processData: false,
      async: true,
      success: function (data) {
        $("#result").fadeIn(600);
        $("#result").text("Looks like it's " + data + " here.");
        console.log("Success!");
      },
    });
  });
});
