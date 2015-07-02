#!/bin/sh
mkdir /home/powerpancho/Tarea3_201122766

cp Aplicacion.py /home/powerpancho/Tarea3_201122766

cp [SO2]Tarea3_201122766 /etc/init.d

update-rc.d [SO2]Tarea3_201122766 defaults

echo "Debe reiniciar el sistema. Insercion de servicio exitosamente"
