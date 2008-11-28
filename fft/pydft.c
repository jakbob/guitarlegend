/* Generated by Cython 0.9.8.1.1 on Fri Nov 28 23:46:33 2008 */

#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "structmember.h"
#ifndef PY_LONG_LONG
  #define PY_LONG_LONG LONG_LONG
#endif
#ifndef DL_EXPORT
  #define DL_EXPORT(t) t
#endif
#if PY_VERSION_HEX < 0x02040000
  #define METH_COEXIST 0
#endif
#if PY_VERSION_HEX < 0x02050000
  typedef int Py_ssize_t;
  #define PY_SSIZE_T_MAX INT_MAX
  #define PY_SSIZE_T_MIN INT_MIN
  #define PyInt_FromSsize_t(z) PyInt_FromLong(z)
  #define PyInt_AsSsize_t(o)   PyInt_AsLong(o)
  #define PyNumber_Index(o)    PyNumber_Int(o)
  #define PyIndex_Check(o)     PyNumber_Check(o)
#endif
#if PY_VERSION_HEX < 0x02060000
  #define Py_REFCNT(ob) (((PyObject*)(ob))->ob_refcnt)
  #define Py_TYPE(ob)   (((PyObject*)(ob))->ob_type)
  #define Py_SIZE(ob)   (((PyVarObject*)(ob))->ob_size)
  #define PyVarObject_HEAD_INIT(type, size) \
          PyObject_HEAD_INIT(type) size,
  #define PyType_Modified(t)

  typedef struct {
       void *buf;
       Py_ssize_t len;
       int readonly;
       const char *format;
       int ndim;
       Py_ssize_t *shape;
       Py_ssize_t *strides;
       Py_ssize_t *suboffsets;
       Py_ssize_t itemsize;
       void *internal;
  } Py_buffer;

  #define PyBUF_SIMPLE 0
  #define PyBUF_WRITABLE 0x0001
  #define PyBUF_LOCK 0x0002
  #define PyBUF_FORMAT 0x0004
  #define PyBUF_ND 0x0008
  #define PyBUF_STRIDES (0x0010 | PyBUF_ND)
  #define PyBUF_C_CONTIGUOUS (0x0020 | PyBUF_STRIDES)
  #define PyBUF_F_CONTIGUOUS (0x0040 | PyBUF_STRIDES)
  #define PyBUF_ANY_CONTIGUOUS (0x0080 | PyBUF_STRIDES)
  #define PyBUF_INDIRECT (0x0100 | PyBUF_STRIDES)

#endif
#if PY_MAJOR_VERSION < 3
  #define __Pyx_BUILTIN_MODULE_NAME "__builtin__"
#else
  #define __Pyx_BUILTIN_MODULE_NAME "builtins"
#endif
#if PY_MAJOR_VERSION >= 3
  #define Py_TPFLAGS_CHECKTYPES 0
  #define Py_TPFLAGS_HAVE_INDEX 0
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBaseString_Type            PyUnicode_Type
  #define PyString_Type                PyBytes_Type
  #define PyInt_Type                   PyLong_Type
  #define PyInt_Check(op)              PyLong_Check(op)
  #define PyInt_CheckExact(op)         PyLong_CheckExact(op)
  #define PyInt_FromString             PyLong_FromString
  #define PyInt_FromUnicode            PyLong_FromUnicode
  #define PyInt_FromLong               PyLong_FromLong
  #define PyInt_FromSize_t             PyLong_FromSize_t
  #define PyInt_FromSsize_t            PyLong_FromSsize_t
  #define PyInt_AsLong                 PyLong_AsLong
  #define PyInt_AS_LONG                PyLong_AS_LONG
  #define PyInt_AsSsize_t              PyLong_AsSsize_t
  #define PyInt_AsUnsignedLongMask     PyLong_AsUnsignedLongMask
  #define PyInt_AsUnsignedLongLongMask PyLong_AsUnsignedLongLongMask
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_TrueDivide(x,y)
#else
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_Divide(x,y)
  #define PyBytes_Type                 PyString_Type
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyMethod_New(func, self, klass) PyInstanceMethod_New(func)
#endif
#if !defined(WIN32) && !defined(MS_WINDOWS)
  #ifndef __stdcall
    #define __stdcall
  #endif
  #ifndef __cdecl
    #define __cdecl
  #endif
#else
  #define _USE_MATH_DEFINES
#endif
#ifdef __cplusplus
#define __PYX_EXTERN_C extern "C"
#else
#define __PYX_EXTERN_C extern
#endif
#include <math.h>
#define __PYX_HAVE_API__pydft
#include "math.h"
#include "stdlib.h"


#ifdef __GNUC__
#define INLINE __inline__
#elif _WIN32
#define INLINE __inline
#else
#define INLINE 
#endif

typedef struct {PyObject **p; char *s; long n; char is_unicode; char intern; char is_identifier;} __Pyx_StringTabEntry; /*proto*/



static int __pyx_skip_dispatch = 0;


/* Type Conversion Predeclarations */

#if PY_MAJOR_VERSION < 3
#define __Pyx_PyBytes_FromString PyString_FromString
#define __Pyx_PyBytes_AsString   PyString_AsString
#else
#define __Pyx_PyBytes_FromString PyBytes_FromString
#define __Pyx_PyBytes_AsString   PyBytes_AsString
#endif

#define __Pyx_PyBool_FromLong(b) ((b) ? (Py_INCREF(Py_True), Py_True) : (Py_INCREF(Py_False), Py_False))
static INLINE int __Pyx_PyObject_IsTrue(PyObject* x);
static INLINE PY_LONG_LONG __pyx_PyInt_AsLongLong(PyObject* x);
static INLINE unsigned PY_LONG_LONG __pyx_PyInt_AsUnsignedLongLong(PyObject* x);
static INLINE Py_ssize_t __pyx_PyIndex_AsSsize_t(PyObject* b);

#define __pyx_PyInt_AsLong(x) (PyInt_CheckExact(x) ? PyInt_AS_LONG(x) : PyInt_AsLong(x))
#define __pyx_PyFloat_AsDouble(x) (PyFloat_CheckExact(x) ? PyFloat_AS_DOUBLE(x) : PyFloat_AsDouble(x))

static INLINE unsigned char __pyx_PyInt_unsigned_char(PyObject* x);
static INLINE unsigned short __pyx_PyInt_unsigned_short(PyObject* x);
static INLINE char __pyx_PyInt_char(PyObject* x);
static INLINE short __pyx_PyInt_short(PyObject* x);
static INLINE int __pyx_PyInt_int(PyObject* x);
static INLINE long __pyx_PyInt_long(PyObject* x);
static INLINE signed char __pyx_PyInt_signed_char(PyObject* x);
static INLINE signed short __pyx_PyInt_signed_short(PyObject* x);
static INLINE signed int __pyx_PyInt_signed_int(PyObject* x);
static INLINE signed long __pyx_PyInt_signed_long(PyObject* x);
static INLINE long double __pyx_PyInt_long_double(PyObject* x);
#ifdef __GNUC__
/* Test for GCC > 2.95 */
#if __GNUC__ > 2 ||               (__GNUC__ == 2 && (__GNUC_MINOR__ > 95)) 
#define likely(x)   __builtin_expect(!!(x), 1)
#define unlikely(x) __builtin_expect(!!(x), 0)
#else /* __GNUC__ > 2 ... */
#define likely(x)   (x)
#define unlikely(x) (x)
#endif /* __GNUC__ > 2 ... */
#else /* __GNUC__ */
#define likely(x)   (x)
#define unlikely(x) (x)
#endif /* __GNUC__ */
    
static PyObject *__pyx_m;
static PyObject *__pyx_b;
static PyObject *__pyx_empty_tuple;
static int __pyx_lineno;
static int __pyx_clineno = 0;
static const char * __pyx_cfilenm= __FILE__;
static const char *__pyx_filename;
static const char **__pyx_f;

static INLINE PyObject *__Pyx_GetItemInt(PyObject *o, Py_ssize_t i, int is_unsigned) {
    PyObject *r;
    if (PyList_CheckExact(o) && 0 <= i && i < PyList_GET_SIZE(o)) {
        r = PyList_GET_ITEM(o, i);
        Py_INCREF(r);
    }
    else if (PyTuple_CheckExact(o) && 0 <= i && i < PyTuple_GET_SIZE(o)) {
        r = PyTuple_GET_ITEM(o, i);
        Py_INCREF(r);
    }
    else if (Py_TYPE(o)->tp_as_sequence && Py_TYPE(o)->tp_as_sequence->sq_item && (likely(i >= 0) || !is_unsigned))
        r = PySequence_GetItem(o, i);
    else {
        PyObject *j = (likely(i >= 0) || !is_unsigned) ? PyInt_FromLong(i) : PyLong_FromUnsignedLongLong((sizeof(unsigned long long) > sizeof(Py_ssize_t) ? (1ULL << (sizeof(Py_ssize_t)*8)) : 0) + i);
        if (!j)
            return 0;
        r = PyObject_GetItem(o, j);
        Py_DECREF(j);
    }
    return r;
}

static INLINE PyObject* __Pyx_PyObject_Append(PyObject* L, PyObject* x) {
    if (likely(PyList_CheckExact(L))) {
        if (PyList_Append(L, x) < 0) return NULL;
        Py_INCREF(Py_None);
        return Py_None; // this is just to have an accurate signature
    }
    else {
        return PyObject_CallMethod(L, "append", "(O)", x);
    }
}

static void __Pyx_AddTraceback(const char *funcname); /*proto*/

static int __Pyx_InitStrings(__Pyx_StringTabEntry *t); /*proto*/

/* Type declarations */

/* "/mnt/usbpen/guitarlegend/fft/pydft.pyx":15
 *     void free(void * ptr)
 * 
 * cdef struct complex:             # <<<<<<<<<<<<<<
 *     double re
 *     double im
 */

struct __pyx_t_5pydft_complex {
  double re;
  double im;
};
/* Module declarations from pydft */

__PYX_EXTERN_C DL_EXPORT(struct __pyx_t_5pydft_complex) *DFT(float *, int); /*proto*/


/* Implementation of pydft */
static char __pyx_k_append[] = "append";
static PyObject *__pyx_kp_append;

/* "/mnt/usbpen/guitarlegend/fft/pydft.pyx":21
 * cdef extern complex* c_DFT "DFT" (float * data_points, int N)
 * 
 * def DFT(data):             # <<<<<<<<<<<<<<
 *     """Perform the Discrete Fourier Transform.
 * 
 */

static PyObject *__pyx_pf_5pydft_DFT(PyObject *__pyx_self, PyObject *__pyx_v_data); /*proto*/
static char __pyx_doc_5pydft_DFT[] = "Perform the Discrete Fourier Transform.\n\n    Arguments\n    data -- iterable of the samples on which to perform the transform\n\n    Returns\n    freq -- list of the magnitudes of the frequencies. Yes, we need to change this.";
static PyObject *__pyx_pf_5pydft_DFT(PyObject *__pyx_self, PyObject *__pyx_v_data) {
  struct __pyx_t_5pydft_complex *__pyx_v_freqs;
  float *__pyx_v_cdata;
  int __pyx_v_i;
  int __pyx_v_N;
  PyObject *__pyx_v_pyfreqs;
  PyObject *__pyx_r;
  Py_ssize_t __pyx_1 = 0;
  PyObject *__pyx_2 = 0;
  float __pyx_3;
  PyObject *__pyx_4 = 0;
  __pyx_self = __pyx_self;
  __pyx_v_pyfreqs = Py_None; Py_INCREF(Py_None);

  /* "/mnt/usbpen/guitarlegend/fft/pydft.pyx":34
 *     cdef int i, N
 * 
 *     N = len(data)             # <<<<<<<<<<<<<<
 * 
 *     # Convert python list to C array of floats
 */
  __pyx_1 = PyObject_Length(__pyx_v_data); if (unlikely(__pyx_1 == -1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 34; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __pyx_v_N = __pyx_1;

  /* "/mnt/usbpen/guitarlegend/fft/pydft.pyx":37
 * 
 *     # Convert python list to C array of floats
 *     cdata = <float *>malloc(sizeof(float)*N)             # <<<<<<<<<<<<<<
 *     for i from 0 <= i < N:
 *         # Apparently, this method is slow. One should use PyTuple_GET_ITEM and PyMem_Malloc
 */
  __pyx_v_cdata = ((float *)malloc(((sizeof(float)) * __pyx_v_N)));

  /* "/mnt/usbpen/guitarlegend/fft/pydft.pyx":38
 *     # Convert python list to C array of floats
 *     cdata = <float *>malloc(sizeof(float)*N)
 *     for i from 0 <= i < N:             # <<<<<<<<<<<<<<
 *         # Apparently, this method is slow. One should use PyTuple_GET_ITEM and PyMem_Malloc
 *         # from Python.h unless you use a new version of Cython. The former gives me a
 */
  for (__pyx_v_i = 0; __pyx_v_i < __pyx_v_N; __pyx_v_i++) {

    /* "/mnt/usbpen/guitarlegend/fft/pydft.pyx":43
 *         # segfault, though.
 *         # TODO: Fix this.
 *         cdata[i] = data[i]             # <<<<<<<<<<<<<<
 * 
 *     # Perform the DFT
 */
    __pyx_2 = __Pyx_GetItemInt(__pyx_v_data, __pyx_v_i, 0); if (!__pyx_2) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 43; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __pyx_3 = __pyx_PyFloat_AsDouble(__pyx_2); if (unlikely(PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 43; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    Py_DECREF(__pyx_2); __pyx_2 = 0;
    (__pyx_v_cdata[__pyx_v_i]) = __pyx_3;
  }

  /* "/mnt/usbpen/guitarlegend/fft/pydft.pyx":46
 * 
 *     # Perform the DFT
 *     freqs = c_DFT(cdata, N)             # <<<<<<<<<<<<<<
 * 
 *     # Copy the data back to a Python list. I know that calculating the
 */
  __pyx_v_freqs = DFT(__pyx_v_cdata, __pyx_v_N);

  /* "/mnt/usbpen/guitarlegend/fft/pydft.pyx":51
 *     # magnitude means extra overhead, but this is for testing purposes.
 *     # TODO: Fix this.
 *     pyfreqs = []             # <<<<<<<<<<<<<<
 *     for i from 0 <= i < N:
 *         pyfreqs.append(sqrt(freqs[i].re**2 + freqs[i].im**2))
 */
  __pyx_2 = PyList_New(0); if (unlikely(!__pyx_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 51; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  Py_DECREF(__pyx_v_pyfreqs);
  __pyx_v_pyfreqs = ((PyObject *)__pyx_2);
  __pyx_2 = 0;

  /* "/mnt/usbpen/guitarlegend/fft/pydft.pyx":52
 *     # TODO: Fix this.
 *     pyfreqs = []
 *     for i from 0 <= i < N:             # <<<<<<<<<<<<<<
 *         pyfreqs.append(sqrt(freqs[i].re**2 + freqs[i].im**2))
 * 
 */
  for (__pyx_v_i = 0; __pyx_v_i < __pyx_v_N; __pyx_v_i++) {

    /* "/mnt/usbpen/guitarlegend/fft/pydft.pyx":53
 *     pyfreqs = []
 *     for i from 0 <= i < N:
 *         pyfreqs.append(sqrt(freqs[i].re**2 + freqs[i].im**2))             # <<<<<<<<<<<<<<
 * 
 *     # Free those little fuckers
 */
    __pyx_2 = PyFloat_FromDouble(sqrt((pow((__pyx_v_freqs[__pyx_v_i]).re, 2) + pow((__pyx_v_freqs[__pyx_v_i]).im, 2)))); if (unlikely(!__pyx_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 53; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    __pyx_4 = __Pyx_PyObject_Append(__pyx_v_pyfreqs, __pyx_2); if (unlikely(!__pyx_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 53; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    Py_DECREF(__pyx_2); __pyx_2 = 0;
    Py_DECREF(__pyx_4); __pyx_4 = 0;
  }

  /* "/mnt/usbpen/guitarlegend/fft/pydft.pyx":56
 * 
 *     # Free those little fuckers
 *     free(freqs)             # <<<<<<<<<<<<<<
 *     free(cdata)
 * 
 */
  free(__pyx_v_freqs);

  /* "/mnt/usbpen/guitarlegend/fft/pydft.pyx":57
 *     # Free those little fuckers
 *     free(freqs)
 *     free(cdata)             # <<<<<<<<<<<<<<
 * 
 *     return pyfreqs
 */
  free(__pyx_v_cdata);

  /* "/mnt/usbpen/guitarlegend/fft/pydft.pyx":59
 *     free(cdata)
 * 
 *     return pyfreqs             # <<<<<<<<<<<<<<
 */
  Py_INCREF(__pyx_v_pyfreqs);
  __pyx_r = __pyx_v_pyfreqs;
  goto __pyx_L0;

  __pyx_r = Py_None; Py_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  Py_XDECREF(__pyx_2);
  Py_XDECREF(__pyx_4);
  __Pyx_AddTraceback("pydft.DFT");
  __pyx_r = NULL;
  __pyx_L0:;
  Py_DECREF(__pyx_v_pyfreqs);
  return __pyx_r;
}

static struct PyMethodDef __pyx_methods[] = {
  {"DFT", (PyCFunction)__pyx_pf_5pydft_DFT, METH_O, __pyx_doc_5pydft_DFT},
  {0, 0, 0, 0}
};

static void __pyx_init_filenames(void); /*proto*/

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef __pyx_moduledef = {
    PyModuleDef_HEAD_INIT,
    "pydft",
    0, /* m_doc */
    -1, /* m_size */
    __pyx_methods /* m_methods */,
    NULL, /* m_reload */
    NULL, /* m_traverse */
    NULL, /* m_clear */
    NULL /* m_free */
};
#endif

static __Pyx_StringTabEntry __pyx_string_tab[] = {
  {&__pyx_kp_append, __pyx_k_append, sizeof(__pyx_k_append), 1, 1, 1},
  {0, 0, 0, 0, 0, 0}
};
static int __Pyx_InitCachedBuiltins(void) {
  return 0;
  return -1;
}

static int __Pyx_InitGlobals(void) {
  if (__Pyx_InitStrings(__pyx_string_tab) < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;};
  return 0;
  __pyx_L1_error:;
  return -1;
}

#if PY_MAJOR_VERSION < 3
PyMODINIT_FUNC initpydft(void); /*proto*/
PyMODINIT_FUNC initpydft(void)
#else
PyMODINIT_FUNC PyInit_pydft(void); /*proto*/
PyMODINIT_FUNC PyInit_pydft(void)
#endif
{
  __pyx_empty_tuple = PyTuple_New(0); if (unlikely(!__pyx_empty_tuple)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  /*--- Libary function declarations ---*/
  __pyx_init_filenames();
  /*--- Initialize various global constants etc. ---*/
  if (unlikely(__Pyx_InitGlobals() < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  /*--- Module creation code ---*/
  #if PY_MAJOR_VERSION < 3
  __pyx_m = Py_InitModule4("pydft", __pyx_methods, 0, 0, PYTHON_API_VERSION);
  #else
  __pyx_m = PyModule_Create(&__pyx_moduledef);
  #endif
  if (!__pyx_m) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;};
  #if PY_MAJOR_VERSION < 3
  Py_INCREF(__pyx_m);
  #endif
  __pyx_b = PyImport_AddModule(__Pyx_BUILTIN_MODULE_NAME);
  if (!__pyx_b) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;};
  if (PyObject_SetAttrString(__pyx_m, "__builtins__", __pyx_b) < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;};
  /*--- Builtin init code ---*/
  if (unlikely(__Pyx_InitCachedBuiltins() < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __pyx_skip_dispatch = 0;
  /*--- Global init code ---*/
  /*--- Function export code ---*/
  /*--- Type init code ---*/
  /*--- Type import code ---*/
  /*--- Function import code ---*/
  /*--- Execution code ---*/

  /* "/mnt/usbpen/guitarlegend/fft/pydft.pyx":21
 * cdef extern complex* c_DFT "DFT" (float * data_points, int N)
 * 
 * def DFT(data):             # <<<<<<<<<<<<<<
 *     """Perform the Discrete Fourier Transform.
 * 
 */
  #if PY_MAJOR_VERSION < 3
  return;
  #else
  return __pyx_m;
  #endif
  __pyx_L1_error:;
  __Pyx_AddTraceback("pydft");
  #if PY_MAJOR_VERSION >= 3
  return NULL;
  #endif
}

static const char *__pyx_filenames[] = {
  "pydft.pyx",
};

/* Runtime support code */

static void __pyx_init_filenames(void) {
  __pyx_f = __pyx_filenames;
}


#include "compile.h"
#include "frameobject.h"
#include "traceback.h"

static void __Pyx_AddTraceback(const char *funcname) {
    PyObject *py_srcfile = 0;
    PyObject *py_funcname = 0;
    PyObject *py_globals = 0;
    PyObject *empty_string = 0;
    PyCodeObject *py_code = 0;
    PyFrameObject *py_frame = 0;

    #if PY_MAJOR_VERSION < 3
    py_srcfile = PyString_FromString(__pyx_filename);
    #else
    py_srcfile = PyUnicode_FromString(__pyx_filename);
    #endif
    if (!py_srcfile) goto bad;
    if (__pyx_clineno) {
        #if PY_MAJOR_VERSION < 3
        py_funcname = PyString_FromFormat( "%s (%s:%d)", funcname, __pyx_cfilenm, __pyx_clineno);
        #else
        py_funcname = PyUnicode_FromFormat( "%s (%s:%d)", funcname, __pyx_cfilenm, __pyx_clineno);
        #endif
    }
    else {
        #if PY_MAJOR_VERSION < 3
        py_funcname = PyString_FromString(funcname);
        #else
        py_funcname = PyUnicode_FromString(funcname);
        #endif
    }
    if (!py_funcname) goto bad;
    py_globals = PyModule_GetDict(__pyx_m);
    if (!py_globals) goto bad;
    #if PY_MAJOR_VERSION < 3
    empty_string = PyString_FromStringAndSize("", 0);
    #else
    empty_string = PyBytes_FromStringAndSize("", 0);
    #endif
    if (!empty_string) goto bad;
    py_code = PyCode_New(
        0,            /*int argcount,*/
        #if PY_MAJOR_VERSION >= 3
        0,            /*int kwonlyargcount,*/
        #endif
        0,            /*int nlocals,*/
        0,            /*int stacksize,*/
        0,            /*int flags,*/
        empty_string, /*PyObject *code,*/
        __pyx_empty_tuple,  /*PyObject *consts,*/
        __pyx_empty_tuple,  /*PyObject *names,*/
        __pyx_empty_tuple,  /*PyObject *varnames,*/
        __pyx_empty_tuple,  /*PyObject *freevars,*/
        __pyx_empty_tuple,  /*PyObject *cellvars,*/
        py_srcfile,   /*PyObject *filename,*/
        py_funcname,  /*PyObject *name,*/
        __pyx_lineno,   /*int firstlineno,*/
        empty_string  /*PyObject *lnotab*/
    );
    if (!py_code) goto bad;
    py_frame = PyFrame_New(
        PyThreadState_Get(), /*PyThreadState *tstate,*/
        py_code,             /*PyCodeObject *code,*/
        py_globals,          /*PyObject *globals,*/
        0                    /*PyObject *locals*/
    );
    if (!py_frame) goto bad;
    py_frame->f_lineno = __pyx_lineno;
    PyTraceBack_Here(py_frame);
bad:
    Py_XDECREF(py_srcfile);
    Py_XDECREF(py_funcname);
    Py_XDECREF(empty_string);
    Py_XDECREF(py_code);
    Py_XDECREF(py_frame);
}

static int __Pyx_InitStrings(__Pyx_StringTabEntry *t) {
    while (t->p) {
        #if PY_MAJOR_VERSION < 3
        if (t->is_unicode && (!t->is_identifier)) {
            *t->p = PyUnicode_DecodeUTF8(t->s, t->n - 1, NULL);
        } else if (t->intern) {
            *t->p = PyString_InternFromString(t->s);
        } else {
            *t->p = PyString_FromStringAndSize(t->s, t->n - 1);
        }
        #else  /* Python 3+ has unicode identifiers */
        if (t->is_identifier || (t->is_unicode && t->intern)) {
            *t->p = PyUnicode_InternFromString(t->s);
        } else if (t->is_unicode) {
            *t->p = PyUnicode_FromStringAndSize(t->s, t->n - 1);
        } else {
            *t->p = PyBytes_FromStringAndSize(t->s, t->n - 1);
        }
        #endif
        if (!*t->p)
            return -1;
        ++t;
    }
    return 0;
}

/* Type Conversion Functions */

static INLINE Py_ssize_t __pyx_PyIndex_AsSsize_t(PyObject* b) {
  Py_ssize_t ival;
  PyObject* x = PyNumber_Index(b);
  if (!x) return -1;
  ival = PyInt_AsSsize_t(x);
  Py_DECREF(x);
  return ival;
}

static INLINE int __Pyx_PyObject_IsTrue(PyObject* x) {
   if (x == Py_True) return 1;
   else if (x == Py_False) return 0;
   else return PyObject_IsTrue(x);
}

static INLINE PY_LONG_LONG __pyx_PyInt_AsLongLong(PyObject* x) {
    if (PyInt_CheckExact(x)) {
        return PyInt_AS_LONG(x);
    }
    else if (PyLong_CheckExact(x)) {
        return PyLong_AsLongLong(x);
    }
    else {
        PY_LONG_LONG val;
        PyObject* tmp = PyNumber_Int(x); if (!tmp) return (PY_LONG_LONG)-1;
        val = __pyx_PyInt_AsLongLong(tmp);
        Py_DECREF(tmp);
        return val;
    }
}

static INLINE unsigned PY_LONG_LONG __pyx_PyInt_AsUnsignedLongLong(PyObject* x) {
    if (PyInt_CheckExact(x)) {
        long val = PyInt_AS_LONG(x);
        if (unlikely(val < 0)) {
            PyErr_SetString(PyExc_TypeError, "Negative assignment to unsigned type.");
            return (unsigned PY_LONG_LONG)-1;
        }
        return val;
    }
    else if (PyLong_CheckExact(x)) {
        return PyLong_AsUnsignedLongLong(x);
    }
    else {
        PY_LONG_LONG val;
        PyObject* tmp = PyNumber_Int(x); if (!tmp) return (PY_LONG_LONG)-1;
        val = __pyx_PyInt_AsUnsignedLongLong(tmp);
        Py_DECREF(tmp);
        return val;
    }
}


static INLINE unsigned char __pyx_PyInt_unsigned_char(PyObject* x) {
    if (sizeof(unsigned char) < sizeof(long)) {
        long long_val = __pyx_PyInt_AsLong(x);
        unsigned char val = (unsigned char)long_val;
        if (unlikely((val != long_val)  || (long_val < 0))) {
            PyErr_SetString(PyExc_OverflowError, "value too large to convert to unsigned char");
            return (unsigned char)-1;
        }
        return val;
    }
    else {
        return __pyx_PyInt_AsLong(x);
    }
}

static INLINE unsigned short __pyx_PyInt_unsigned_short(PyObject* x) {
    if (sizeof(unsigned short) < sizeof(long)) {
        long long_val = __pyx_PyInt_AsLong(x);
        unsigned short val = (unsigned short)long_val;
        if (unlikely((val != long_val)  || (long_val < 0))) {
            PyErr_SetString(PyExc_OverflowError, "value too large to convert to unsigned short");
            return (unsigned short)-1;
        }
        return val;
    }
    else {
        return __pyx_PyInt_AsLong(x);
    }
}

static INLINE char __pyx_PyInt_char(PyObject* x) {
    if (sizeof(char) < sizeof(long)) {
        long long_val = __pyx_PyInt_AsLong(x);
        char val = (char)long_val;
        if (unlikely((val != long_val) )) {
            PyErr_SetString(PyExc_OverflowError, "value too large to convert to char");
            return (char)-1;
        }
        return val;
    }
    else {
        return __pyx_PyInt_AsLong(x);
    }
}

static INLINE short __pyx_PyInt_short(PyObject* x) {
    if (sizeof(short) < sizeof(long)) {
        long long_val = __pyx_PyInt_AsLong(x);
        short val = (short)long_val;
        if (unlikely((val != long_val) )) {
            PyErr_SetString(PyExc_OverflowError, "value too large to convert to short");
            return (short)-1;
        }
        return val;
    }
    else {
        return __pyx_PyInt_AsLong(x);
    }
}

static INLINE int __pyx_PyInt_int(PyObject* x) {
    if (sizeof(int) < sizeof(long)) {
        long long_val = __pyx_PyInt_AsLong(x);
        int val = (int)long_val;
        if (unlikely((val != long_val) )) {
            PyErr_SetString(PyExc_OverflowError, "value too large to convert to int");
            return (int)-1;
        }
        return val;
    }
    else {
        return __pyx_PyInt_AsLong(x);
    }
}

static INLINE long __pyx_PyInt_long(PyObject* x) {
    if (sizeof(long) < sizeof(long)) {
        long long_val = __pyx_PyInt_AsLong(x);
        long val = (long)long_val;
        if (unlikely((val != long_val) )) {
            PyErr_SetString(PyExc_OverflowError, "value too large to convert to long");
            return (long)-1;
        }
        return val;
    }
    else {
        return __pyx_PyInt_AsLong(x);
    }
}

static INLINE signed char __pyx_PyInt_signed_char(PyObject* x) {
    if (sizeof(signed char) < sizeof(long)) {
        long long_val = __pyx_PyInt_AsLong(x);
        signed char val = (signed char)long_val;
        if (unlikely((val != long_val) )) {
            PyErr_SetString(PyExc_OverflowError, "value too large to convert to signed char");
            return (signed char)-1;
        }
        return val;
    }
    else {
        return __pyx_PyInt_AsLong(x);
    }
}

static INLINE signed short __pyx_PyInt_signed_short(PyObject* x) {
    if (sizeof(signed short) < sizeof(long)) {
        long long_val = __pyx_PyInt_AsLong(x);
        signed short val = (signed short)long_val;
        if (unlikely((val != long_val) )) {
            PyErr_SetString(PyExc_OverflowError, "value too large to convert to signed short");
            return (signed short)-1;
        }
        return val;
    }
    else {
        return __pyx_PyInt_AsLong(x);
    }
}

static INLINE signed int __pyx_PyInt_signed_int(PyObject* x) {
    if (sizeof(signed int) < sizeof(long)) {
        long long_val = __pyx_PyInt_AsLong(x);
        signed int val = (signed int)long_val;
        if (unlikely((val != long_val) )) {
            PyErr_SetString(PyExc_OverflowError, "value too large to convert to signed int");
            return (signed int)-1;
        }
        return val;
    }
    else {
        return __pyx_PyInt_AsLong(x);
    }
}

static INLINE signed long __pyx_PyInt_signed_long(PyObject* x) {
    if (sizeof(signed long) < sizeof(long)) {
        long long_val = __pyx_PyInt_AsLong(x);
        signed long val = (signed long)long_val;
        if (unlikely((val != long_val) )) {
            PyErr_SetString(PyExc_OverflowError, "value too large to convert to signed long");
            return (signed long)-1;
        }
        return val;
    }
    else {
        return __pyx_PyInt_AsLong(x);
    }
}

static INLINE long double __pyx_PyInt_long_double(PyObject* x) {
    if (sizeof(long double) < sizeof(long)) {
        long long_val = __pyx_PyInt_AsLong(x);
        long double val = (long double)long_val;
        if (unlikely((val != long_val) )) {
            PyErr_SetString(PyExc_OverflowError, "value too large to convert to long double");
            return (long double)-1;
        }
        return val;
    }
    else {
        return __pyx_PyInt_AsLong(x);
    }
}

