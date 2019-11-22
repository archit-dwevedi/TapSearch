$('#word').on("input", function() {
    $.ajax({
        type: 'POST',
        url: '/documents/search',
        data: {
            word_ajax: $('#word').val(),
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