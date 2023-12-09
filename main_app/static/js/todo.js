$(document).ready(function() {
    var tasks = [];

    $('.form__submit-button').click(function() {
        var newTaskContent = $('#new-task').val().trim();
        if (newTaskContent) {
            tasks.push(newTaskContent); 
            updateTasks();
            $('#new-task').val(''); 
        }
    });

    function updateTasks() {
        $('#tasks').empty(); 
        $.each(tasks, function(index, task) {
            var taskId = 'task' + index;
            $('#tasks').append(
                $('<div>').addClass('task').append(
                    $('<input>').addClass('form__input-checkbox').attr('type', 'checkbox').attr('id', taskId),
                    $('<label>').addClass('form__input-label').attr('for', taskId).text(task),
                    $('<span>').addClass('fa fa-times remove-task').click(function() {
                        
                        tasks.splice(index, 1);
                        updateTasks();
                    })
                )
            );
        });
    }

    
    $(document).on('change', '.form__input-checkbox', function() {
    });
});
