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
                        // 移除任务并更新数组
                        tasks.splice(index, 1);
                        updateTasks();
                    })
                )
            );
        });
    }

    // 当复选框状态改变时，更新任务样式（如果需要）
    $(document).on('change', '.form__input-checkbox', function() {
        // 这里可以添加任何需要在选中复选框时执行的逻辑
    });
});
