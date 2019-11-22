$('#word').on("input", function() {
    $.ajax({
        type: 'POST',
        url: '/documents/search',
        data: {
            word_ajax: $('#word').val(),
            by_word_ajax: document.getElementById('id-name--1').checked,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        cache: false,
        dataType: "html",
        success: function(data) {

            var content = document.getElementById('content');
            content.innerHTML = data;
        }
    });
});


function toggle() {
    // alert("toggle")
    // alert(document.getElementById('id-name--1').checked);
    // document.getElementById('id-name--1').checked = (document.getElementById('id-name--1').checked);
    // alert(document.getElementById('id-name--1').checked);
}