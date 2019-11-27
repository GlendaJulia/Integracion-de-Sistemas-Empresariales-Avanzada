var Odoo = require("odoo-xmlrpc");

var odoo = new Odoo({
    url: "localhost",
    port: "8069",
    db: "tecsup_odoo_puntoventa",
    username: "admin",
    password: "admin"
});

odoo.connect(function(err){
    if (err){
        return(console.log(err));
    }
    console.log("Conectado al servicio de Odoo");
    var inParams = [];
    inParams.push([]);
    var params = [];
    params.push(inParams);
    odoo.execute_kw("facturacion.series","search_read",params, function(
        err,
        value
    ){
        if(err){
            return console.log(err);
        }
        console.log("Result: ", value);
    });
});