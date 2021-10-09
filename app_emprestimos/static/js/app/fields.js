function FieldsController(){

}

FieldsController.prototype = {
    init: function(){
        this.initDateRangeFields();
    },
    initDateRangeFields: function(){
        $('.date-input').each(function(i, element){
            $(element).datetimepicker({
               lang: 'pt',
               timepicker: false,
               format: 'd/m/Y',
               scrollMonth: false,
               scrollTime: false,
               scrollInput: false
            });
        });
        $('.date-time-input').each(function(i, element){
            $(element).datetimepicker({
               lang: 'pt',
               timepicker: true,
               format: 'd/m/Y',
               scrollMonth: false,
               scrollTime: true,
               scrollInput: false
            });
        });
    }
}
