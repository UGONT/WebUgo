/* Funcion elegir opcion de formulario */
$(document).ready(function() {
    const $formOption = $('#formOption');
    const $fileOption = $('#fileOption');
    const $comicForm = $('#comicForm');
    const $excelForm = $('#excelForm');

    $formOption.change(function() {
        if ($formOption.is(':checked')) {
            $comicForm.show();
            $excelForm.hide();
        }
    });

    $fileOption.change(function() {
        if ($fileOption.is(':checked')) {
            $comicForm.hide();
            $excelForm.show();
        }
    });
});