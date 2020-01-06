#include <Python.h>
#include <ctype.h>

/*
 * Implements an example function.
 */
PyDoc_STRVAR(generarHorario_example_doc, "example(obj, number)\
\
Example function");


PyObject *generarHorario_generar(PyObject *self, PyObject *args, PyObject *kwargs) {
    /* Shared references that do not need Py_DECREF before returning. */
    PyObject *obj = NULL;

    /*************Variables de soporte para el programa****************/
    FILE* pf; //Apuntdor a archivo
    FILE* pf1; //Apuntdor a archivo
    //char nom[42];
    //char num[7];
    char linea[140];
    char numemp[7];
    char name [41];
    char semana[16][6];
    int i, n, suma;
    int ind = 0;
    int ans = 0;
    char Pag[] = "PROFESOR";
    /******************************************************************/

    const char * nombreArchivo;

    /* Parse positional and keyword arguments */
    if (!PyArg_ParseTuple(args, "s", &nombreArchivo)) {
        return NULL;
    }

    /* Function implementation starts here */

    if (nombreArchivo == NULL) {
        PyErr_SetObject(PyExc_ValueError, obj);
        return NULL;    /* return NULL indicates error */
    }

    else {
        /*Abre el archivo a modificar*/
        pf = fopen(nombreArchivo, "r");
        if (pf == NULL) {
            printf("\n\tNo existe archivo...");
        }

        else {
            /*Crea el archivo en donde se guardara los horarios ya acomodados*/
            pf1 = fopen("horario_generado.cvs", "w+");

            /*Se guarda el formato deseado del archivo*/
            fprintf(pf1, "#N Empleado\tMAESTRO\tHorario\tLunes\tMartes\tMiercoles\tJueves\tViernes\tSabado\n");
            while (fgets(linea, 140, pf)) {

                /*Entra solo si la linea leida empieza con "PROFESOR"*/
                ans = 0;
                if (strncmp(linea, Pag, 8) == 0)
                    ans = 1;

                if (ans) {
                    //numemp = getNEmpl(linea); 
                    /*Obtiene el numero de empleado del prosedor*/

                    i = 0;
                    ind = 10;
                    strcpy(numemp, "      ");
                    while (isdigit(linea[ind]) == 0) {
                        ind++;
                    }
                    while (isdigit(linea[ind + i])) {
                        numemp[i] = linea[ind + i];
                        i++;
                    }
                    //name = getNomEmpl(linea); 

                    /*Obtiene el nombre del empleado*/
                    i = 0;
                    ind = 23;
                    strcpy(name, "                                        ");
                    while (linea[ind + i] != '\n') {
                        name[i] = linea[ind + i];
                        i++;
                    }
                    name[i - 1] = ' ';

                    //fprintf(pf1,"\t%s\t%s\n",numemp,name);

                    for (i = 0; i < 5; i++)
                        fgets(linea, 140, pf);
                    suma = 0;

                    for (i = 0; i < 16; i++) {
                        for (n = 0; n < 6; n++) {
                            if (isdigit(linea[17 + 17 * n])) {
                                semana[i][n] = 'X';
                                suma++;
                            }
                            else
                                semana[i][n] = ' ';
                        }
                        fgets(linea, 140, pf);
                        fgets(linea, 140, pf);
                        fgets(linea, 140, pf);
                    }
                    for (i = 0; i < 16; i++) {
                        fprintf(pf1, "%s\t%s\t%d:00 - %d:00", numemp, name, 7 + i, 8 + i);
                        for (n = 0; n < 6; n++) {
                            fprintf(pf1, "%c\t", semana[i][n]);
                        }
                        fprintf(pf1, "\n");
                    }
                    fprintf(pf1, "%s\t%s\t%d\t", numemp, name, suma);
                    fprintf(pf1, "\n");

                }
            }

                /*Cierre de los archivos abiertos*/
    fclose(pf);
    fclose(pf1);

        }
    }

    Py_RETURN_NONE;
}

/*
 * List of functions to add to generarHorario in exec_generarHorario().
 */
static PyMethodDef generarHorario_functions[] = {
    { "generar", (PyCFunction)generarHorario_generar, METH_VARARGS | METH_KEYWORDS, generarHorario_example_doc },
    { NULL, NULL, 0, NULL } /* marks end of array */
};

/*
 * Initialize generarHorario. May be called multiple times, so avoid
 * using static state.
 */
int exec_generarHorario(PyObject *module) {
    PyModule_AddFunctions(module, generarHorario_functions);

    PyModule_AddStringConstant(module, "__author__", "Estacionamiento UABC");
    PyModule_AddStringConstant(module, "__version__", "1.0.0");
    PyModule_AddIntConstant(module, "year", 2019);

    return 0; /* success */
}

/*
 * Documentation for generarHorario.
 */
PyDoc_STRVAR(generarHorario_doc, "Modulo para exportar el horario de los docnetes en base a un formato dado.");


static PyModuleDef_Slot generarHorario_slots[] = {
    { Py_mod_exec, exec_generarHorario },
    { 0, NULL }
};

static PyModuleDef generarHorario_def = {
    PyModuleDef_HEAD_INIT,
    "generarHorario",
    generarHorario_doc,
    0,              /* m_size */
    NULL,           /* m_methods */
    generarHorario_slots,
    NULL,           /* m_traverse */
    NULL,           /* m_clear */
    NULL,           /* m_free */
};

PyMODINIT_FUNC PyInit_generarHorario() {
    return PyModuleDef_Init(&generarHorario_def);
}
