/* Generated by Cython 0.10.3 on Fri Feb 27 10:52:10 2009 */

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
       PyObject *obj;
       Py_ssize_t len;
       Py_ssize_t itemsize;
       int readonly;
       int ndim;
       char *format;
       Py_ssize_t *shape;
       Py_ssize_t *strides;
       Py_ssize_t *suboffsets;
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
#if (PY_VERSION_HEX < 0x02060000) || (PY_MAJOR_VERSION >= 3)
  #define Py_TPFLAGS_HAVE_NEWBUFFER 0
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
#define __PYX_HAVE_API__wonderful__wonderful
#include "math.h"
#include "stdlib.h"
#include "portaudio.h"
#include "c_wonderful.h"


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

static int __Pyx_Print(PyObject *, int); /*proto*/
#if PY_MAJOR_VERSION >= 3
static PyObject* __pyx_print = 0;
static PyObject* __pyx_print_kwargs = 0;
#endif

static PyObject *__Pyx_GetName(PyObject *dict, PyObject *name); /*proto*/

static void __Pyx_Raise(PyObject *type, PyObject *value, PyObject *tb); /*proto*/

static INLINE void __Pyx_ErrRestore(PyObject *type, PyObject *value, PyObject *tb); /*proto*/
static INLINE void __Pyx_ErrFetch(PyObject **type, PyObject **value, PyObject **tb); /*proto*/

static void __Pyx_AddTraceback(const char *funcname); /*proto*/

static int __Pyx_InitStrings(__Pyx_StringTabEntry *t); /*proto*/

/* Type declarations */

/* "C:\Documents and Settings\Jonne\Desktop\guitarlegend-windist\wonderful/wonderful.pyx":11
 *     void free(void * ptr)
 * 
 * cdef struct complex:             # <<<<<<<<<<<<<<
 *     double re
 *     double im
 */

struct __pyx_t_9wonderful_9wonderful_complex {
  double re;
  double im;
};
/* Module declarations from wonderful.wonderful */

static inputData __pyx_v_9wonderful_9wonderful__input_data;
static PaStream *__pyx_v_9wonderful_9wonderful__stream;
static PyObject *__pyx_f_9wonderful_9wonderful__init(void); /*proto*/
static PyObject *__pyx_f_9wonderful_9wonderful__terminate(void); /*proto*/
static PyObject *__pyx_f_9wonderful_9wonderful__munch(int); /*proto*/


/* Implementation of wonderful.wonderful */
static char __pyx_k_size[] = "size";
static PyObject *__pyx_kp_size;
static char __pyx_k_Exception[] = "Exception";
static PyObject *__pyx_kp_Exception;
static PyObject *__pyx_builtin_Exception;
static PyObject *__pyx_kp_1;
static char __pyx_k_1[] = "An error occurred. I hate you";
static PyObject *__pyx_kp_2;
static char __pyx_k_2[] = "You must call wonderful.init before calling wonderful.munch!";

/* "C:\Documents and Settings\Jonne\Desktop\guitarlegend-windist\wonderful/wonderful.pyx":37
 * cdef PaStream * _stream
 * 
 * cdef _init():             # <<<<<<<<<<<<<<
 *     global _input_data
 *     global _stream
 */

static  PyObject *__pyx_f_9wonderful_9wonderful__init(void) {
  int __pyx_v_err;
  PyObject *__pyx_r;
  PyObject *__pyx_1 = 0;
  PyObject *__pyx_2 = 0;
  int __pyx_3;

  /* "C:\Documents and Settings\Jonne\Desktop\guitarlegend-windist\wonderful/wonderful.pyx":42
 *     cdef int err
 * 
 *     _input_data.samples = ring_buffer_init(1024)             # <<<<<<<<<<<<<<
 *     print <int>_stream
 *     err = wonderful_init(&_input_data, &_stream)
 */
  __pyx_v_9wonderful_9wonderful__input_data.samples = ring_buffer_init(1024);

  /* "C:\Documents and Settings\Jonne\Desktop\guitarlegend-windist\wonderful/wonderful.pyx":43
 * 
 *     _input_data.samples = ring_buffer_init(1024)
 *     print <int>_stream             # <<<<<<<<<<<<<<
 *     err = wonderful_init(&_input_data, &_stream)
 *     if err != 0:
 */
  __pyx_1 = PyInt_FromLong(((int)__pyx_v_9wonderful_9wonderful__stream)); if (unlikely(!__pyx_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 43; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __pyx_2 = PyTuple_New(1); if (unlikely(!__pyx_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 43; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  PyTuple_SET_ITEM(__pyx_2, 0, __pyx_1);
  __pyx_1 = 0;
  if (__Pyx_Print(((PyObject *)__pyx_2), 1) < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 43; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  Py_DECREF(((PyObject *)__pyx_2)); __pyx_2 = 0;

  /* "C:\Documents and Settings\Jonne\Desktop\guitarlegend-windist\wonderful/wonderful.pyx":44
 *     _input_data.samples = ring_buffer_init(1024)
 *     print <int>_stream
 *     err = wonderful_init(&_input_data, &_stream)             # <<<<<<<<<<<<<<
 *     if err != 0:
 *         print "An error occurred. I hate you"
 */
  __pyx_v_err = wonderful_init((&__pyx_v_9wonderful_9wonderful__input_data), (&__pyx_v_9wonderful_9wonderful__stream));

  /* "C:\Documents and Settings\Jonne\Desktop\guitarlegend-windist\wonderful/wonderful.pyx":45
 *     print <int>_stream
 *     err = wonderful_init(&_input_data, &_stream)
 *     if err != 0:             # <<<<<<<<<<<<<<
 *         print "An error occurred. I hate you"
 *     print <int>_stream
 */
  __pyx_3 = (__pyx_v_err != 0);
  if (__pyx_3) {

    /* "C:\Documents and Settings\Jonne\Desktop\guitarlegend-windist\wonderful/wonderful.pyx":46
 *     err = wonderful_init(&_input_data, &_stream)
 *     if err != 0:
 *         print "An error occurred. I hate you"             # <<<<<<<<<<<<<<
 *     print <int>_stream
 * def init():
 */
    __pyx_1 = PyTuple_New(1); if (unlikely(!__pyx_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 46; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    Py_INCREF(__pyx_kp_1);
    PyTuple_SET_ITEM(__pyx_1, 0, __pyx_kp_1);
    if (__Pyx_Print(((PyObject *)__pyx_1), 1) < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 46; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    Py_DECREF(((PyObject *)__pyx_1)); __pyx_1 = 0;
    goto __pyx_L3;
  }
  __pyx_L3:;

  /* "C:\Documents and Settings\Jonne\Desktop\guitarlegend-windist\wonderful/wonderful.pyx":47
 *     if err != 0:
 *         print "An error occurred. I hate you"
 *     print <int>_stream             # <<<<<<<<<<<<<<
 * def init():
 *     """Initialize the wonderful library. This routine MUST be called before the others."""
 */
  __pyx_2 = PyInt_FromLong(((int)__pyx_v_9wonderful_9wonderful__stream)); if (unlikely(!__pyx_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 47; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __pyx_1 = PyTuple_New(1); if (unlikely(!__pyx_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 47; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  PyTuple_SET_ITEM(__pyx_1, 0, __pyx_2);
  __pyx_2 = 0;
  if (__Pyx_Print(((PyObject *)__pyx_1), 1) < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 47; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  Py_DECREF(((PyObject *)__pyx_1)); __pyx_1 = 0;

  __pyx_r = Py_None; Py_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  Py_XDECREF(__pyx_1);
  Py_XDECREF(__pyx_2);
  __Pyx_AddTraceback("wonderful.wonderful._init");
  __pyx_r = 0;
  __pyx_L0:;
  return __pyx_r;
}

/* "C:\Documents and Settings\Jonne\Desktop\guitarlegend-windist\wonderful/wonderful.pyx":48
 *         print "An error occurred. I hate you"
 *     print <int>_stream
 * def init():             # <<<<<<<<<<<<<<
 *     """Initialize the wonderful library. This routine MUST be called before the others."""
 * 
 */

static PyObject *__pyx_pf_9wonderful_9wonderful_init(PyObject *__pyx_self, PyObject *unused); /*proto*/
static char __pyx_doc_9wonderful_9wonderful_init[] = "Initialize the wonderful library. This routine MUST be called before the others.";
static PyObject *__pyx_pf_9wonderful_9wonderful_init(PyObject *__pyx_self, PyObject *unused) {
  PyObject *__pyx_r;
  PyObject *__pyx_1 = 0;
  __pyx_self = __pyx_self;

  /* "C:\Documents and Settings\Jonne\Desktop\guitarlegend-windist\wonderful/wonderful.pyx":51
 *     """Initialize the wonderful library. This routine MUST be called before the others."""
 * 
 *     _init()             # <<<<<<<<<<<<<<
 * 
 * cdef _terminate():
 */
  __pyx_1 = __pyx_f_9wonderful_9wonderful__init(); if (unlikely(!__pyx_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 51; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  Py_DECREF(__pyx_1); __pyx_1 = 0;

  __pyx_r = Py_None; Py_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  Py_XDECREF(__pyx_1);
  __Pyx_AddTraceback("wonderful.wonderful.init");
  __pyx_r = NULL;
  __pyx_L0:;
  return __pyx_r;
}

/* "C:\Documents and Settings\Jonne\Desktop\guitarlegend-windist\wonderful/wonderful.pyx":53
 *     _init()
 * 
 * cdef _terminate():             # <<<<<<<<<<<<<<
 *     global _input_data
 *     global _stream
 */

static  PyObject *__pyx_f_9wonderful_9wonderful__terminate(void) {
  PyObject *__pyx_r;

  /* "C:\Documents and Settings\Jonne\Desktop\guitarlegend-windist\wonderful/wonderful.pyx":57
 *     global _stream
 * 
 *     wonderful_terminate(&_input_data, &_stream)             # <<<<<<<<<<<<<<
 * 
 * def terminate():
 */
  wonderful_terminate((&__pyx_v_9wonderful_9wonderful__input_data), (&__pyx_v_9wonderful_9wonderful__stream));

  __pyx_r = Py_None; Py_INCREF(Py_None);
  return __pyx_r;
}

/* "C:\Documents and Settings\Jonne\Desktop\guitarlegend-windist\wonderful/wonderful.pyx":59
 *     wonderful_terminate(&_input_data, &_stream)
 * 
 * def terminate():             # <<<<<<<<<<<<<<
 *     """Terminate and clean up the wonderful library and kill the portaudio thread.
 *     This routine MUST be called before exiting the program, or the sound might
 */

static PyObject *__pyx_pf_9wonderful_9wonderful_terminate(PyObject *__pyx_self, PyObject *unused); /*proto*/
static char __pyx_doc_9wonderful_9wonderful_terminate[] = "Terminate and clean up the wonderful library and kill the portaudio thread. \n    This routine MUST be called before exiting the program, or the sound might\n    stop working.";
static PyObject *__pyx_pf_9wonderful_9wonderful_terminate(PyObject *__pyx_self, PyObject *unused) {
  PyObject *__pyx_r;
  PyObject *__pyx_1 = 0;
  __pyx_self = __pyx_self;

  /* "C:\Documents and Settings\Jonne\Desktop\guitarlegend-windist\wonderful/wonderful.pyx":64
 *     stop working."""
 * 
 *     _terminate()             # <<<<<<<<<<<<<<
 * 
 * cdef _munch(int size):
 */
  __pyx_1 = __pyx_f_9wonderful_9wonderful__terminate(); if (unlikely(!__pyx_1)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 64; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  Py_DECREF(__pyx_1); __pyx_1 = 0;

  __pyx_r = Py_None; Py_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  Py_XDECREF(__pyx_1);
  __Pyx_AddTraceback("wonderful.wonderful.terminate");
  __pyx_r = NULL;
  __pyx_L0:;
  return __pyx_r;
}

/* "C:\Documents and Settings\Jonne\Desktop\guitarlegend-windist\wonderful/wonderful.pyx":66
 *     _terminate()
 * 
 * cdef _munch(int size):             # <<<<<<<<<<<<<<
 *     global _input_data
 *     global _stream
 */

static  PyObject *__pyx_f_9wonderful_9wonderful__munch(int __pyx_v_size) {
  struct __pyx_t_9wonderful_9wonderful_complex *__pyx_v_dest;
  int __pyx_v_err;
  PyObject *__pyx_r;
  int __pyx_1;
  PyObject *__pyx_2 = 0;
  PyObject *__pyx_3 = 0;

  /* "C:\Documents and Settings\Jonne\Desktop\guitarlegend-windist\wonderful/wonderful.pyx":72
 *     cdef int err
 * 
 *     err = wonderful_munch(&_input_data, dest, 1024)             # <<<<<<<<<<<<<<
 *     if err < 0:
 *         raise Exception("You must call wonderful.init before calling wonderful.munch!")
 */
  __pyx_v_err = wonderful_munch((&__pyx_v_9wonderful_9wonderful__input_data), __pyx_v_dest, 1024);

  /* "C:\Documents and Settings\Jonne\Desktop\guitarlegend-windist\wonderful/wonderful.pyx":73
 * 
 *     err = wonderful_munch(&_input_data, dest, 1024)
 *     if err < 0:             # <<<<<<<<<<<<<<
 *         raise Exception("You must call wonderful.init before calling wonderful.munch!")
 * 
 */
  __pyx_1 = (__pyx_v_err < 0);
  if (__pyx_1) {

    /* "C:\Documents and Settings\Jonne\Desktop\guitarlegend-windist\wonderful/wonderful.pyx":74
 *     err = wonderful_munch(&_input_data, dest, 1024)
 *     if err < 0:
 *         raise Exception("You must call wonderful.init before calling wonderful.munch!")             # <<<<<<<<<<<<<<
 * 
 * def munch(size):
 */
    __pyx_2 = PyTuple_New(1); if (unlikely(!__pyx_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 74; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    Py_INCREF(__pyx_kp_2);
    PyTuple_SET_ITEM(__pyx_2, 0, __pyx_kp_2);
    __pyx_3 = PyObject_Call(__pyx_builtin_Exception, ((PyObject *)__pyx_2), NULL); if (unlikely(!__pyx_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 74; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    Py_DECREF(((PyObject *)__pyx_2)); __pyx_2 = 0;
    __Pyx_Raise(__pyx_3, 0, 0);
    Py_DECREF(__pyx_3); __pyx_3 = 0;
    {__pyx_filename = __pyx_f[0]; __pyx_lineno = 74; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
    goto __pyx_L3;
  }
  __pyx_L3:;

  __pyx_r = Py_None; Py_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  Py_XDECREF(__pyx_2);
  Py_XDECREF(__pyx_3);
  __Pyx_AddTraceback("wonderful.wonderful._munch");
  __pyx_r = 0;
  __pyx_L0:;
  return __pyx_r;
}

/* "C:\Documents and Settings\Jonne\Desktop\guitarlegend-windist\wonderful/wonderful.pyx":76
 *         raise Exception("You must call wonderful.init before calling wonderful.munch!")
 * 
 * def munch(size):             # <<<<<<<<<<<<<<
 *     """Poll for data and return the FFT of it. No data will be returned unless there is
 *     at least size samples available."""
 */

static PyObject *__pyx_pf_9wonderful_9wonderful_munch(PyObject *__pyx_self, PyObject *__pyx_v_size); /*proto*/
static char __pyx_doc_9wonderful_9wonderful_munch[] = "Poll for data and return the FFT of it. No data will be returned unless there is \n    at least size samples available.";
static PyObject *__pyx_pf_9wonderful_9wonderful_munch(PyObject *__pyx_self, PyObject *__pyx_v_size) {
  PyObject *__pyx_r;
  int __pyx_1;
  PyObject *__pyx_2 = 0;
  __pyx_self = __pyx_self;

  /* "C:\Documents and Settings\Jonne\Desktop\guitarlegend-windist\wonderful/wonderful.pyx":80
 *     at least size samples available."""
 * 
 *     _munch(size)             # <<<<<<<<<<<<<<
 */
  __pyx_1 = __pyx_PyInt_int(__pyx_v_size); if (unlikely((__pyx_1 == (int)-1) && PyErr_Occurred())) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 80; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __pyx_2 = __pyx_f_9wonderful_9wonderful__munch(__pyx_1); if (unlikely(!__pyx_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 80; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  Py_DECREF(__pyx_2); __pyx_2 = 0;

  __pyx_r = Py_None; Py_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  Py_XDECREF(__pyx_2);
  __Pyx_AddTraceback("wonderful.wonderful.munch");
  __pyx_r = NULL;
  __pyx_L0:;
  return __pyx_r;
}

static struct PyMethodDef __pyx_methods[] = {
  {"init", (PyCFunction)__pyx_pf_9wonderful_9wonderful_init, METH_NOARGS, __pyx_doc_9wonderful_9wonderful_init},
  {"terminate", (PyCFunction)__pyx_pf_9wonderful_9wonderful_terminate, METH_NOARGS, __pyx_doc_9wonderful_9wonderful_terminate},
  {"munch", (PyCFunction)__pyx_pf_9wonderful_9wonderful_munch, METH_O, __pyx_doc_9wonderful_9wonderful_munch},
  {0, 0, 0, 0}
};

static void __pyx_init_filenames(void); /*proto*/

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef __pyx_moduledef = {
    PyModuleDef_HEAD_INIT,
    "wonderful",
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
  {&__pyx_kp_size, __pyx_k_size, sizeof(__pyx_k_size), 1, 1, 1},
  {&__pyx_kp_Exception, __pyx_k_Exception, sizeof(__pyx_k_Exception), 1, 1, 1},
  {&__pyx_kp_1, __pyx_k_1, sizeof(__pyx_k_1), 0, 0, 0},
  {&__pyx_kp_2, __pyx_k_2, sizeof(__pyx_k_2), 0, 0, 0},
  {0, 0, 0, 0, 0, 0}
};
static int __Pyx_InitCachedBuiltins(void) {
  __pyx_builtin_Exception = __Pyx_GetName(__pyx_b, __pyx_kp_Exception); if (!__pyx_builtin_Exception) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 74; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  return 0;
  __pyx_L1_error:;
  return -1;
}

static int __Pyx_InitGlobals(void) {
  if (__Pyx_InitStrings(__pyx_string_tab) < 0) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;};
  return 0;
  __pyx_L1_error:;
  return -1;
}

#if PY_MAJOR_VERSION < 3
PyMODINIT_FUNC initwonderful(void); /*proto*/
PyMODINIT_FUNC initwonderful(void)
#else
PyMODINIT_FUNC PyInit_wonderful(void); /*proto*/
PyMODINIT_FUNC PyInit_wonderful(void)
#endif
{
  __pyx_empty_tuple = PyTuple_New(0); if (unlikely(!__pyx_empty_tuple)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  /*--- Library function declarations ---*/
  __pyx_init_filenames();
  /*--- Initialize various global constants etc. ---*/
  if (unlikely(__Pyx_InitGlobals() < 0)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 1; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  /*--- Module creation code ---*/
  #if PY_MAJOR_VERSION < 3
  __pyx_m = Py_InitModule4("wonderful", __pyx_methods, 0, 0, PYTHON_API_VERSION);
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

  /* "C:\Documents and Settings\Jonne\Desktop\guitarlegend-windist\wonderful/wonderful.pyx":76
 *         raise Exception("You must call wonderful.init before calling wonderful.munch!")
 * 
 * def munch(size):             # <<<<<<<<<<<<<<
 *     """Poll for data and return the FFT of it. No data will be returned unless there is
 *     at least size samples available."""
 */
  #if PY_MAJOR_VERSION < 3
  return;
  #else
  return __pyx_m;
  #endif
  __pyx_L1_error:;
  __Pyx_AddTraceback("wonderful.wonderful");
  #if PY_MAJOR_VERSION >= 3
  return NULL;
  #endif
}

static const char *__pyx_filenames[] = {
  "wonderful.pyx",
};

/* Runtime support code */

static void __pyx_init_filenames(void) {
  __pyx_f = __pyx_filenames;
}

#if PY_MAJOR_VERSION < 3
static PyObject *__Pyx_GetStdout(void) {
    PyObject *f = PySys_GetObject("stdout");
    if (!f) {
        PyErr_SetString(PyExc_RuntimeError, "lost sys.stdout");
    }
    return f;
}

static int __Pyx_Print(PyObject *arg_tuple, int newline) {
    PyObject *f;
    PyObject* v;
    int i;
    
    if (!(f = __Pyx_GetStdout()))
        return -1;
    for (i=0; i < PyTuple_GET_SIZE(arg_tuple); i++) {
        if (PyFile_SoftSpace(f, 1)) {
            if (PyFile_WriteString(" ", f) < 0)
                return -1;
        }
        v = PyTuple_GET_ITEM(arg_tuple, i);
        if (PyFile_WriteObject(v, f, Py_PRINT_RAW) < 0)
            return -1;
        if (PyString_Check(v)) {
            char *s = PyString_AsString(v);
            Py_ssize_t len = PyString_Size(v);
            if (len > 0 &&
                isspace(Py_CHARMASK(s[len-1])) &&
                s[len-1] != ' ')
                    PyFile_SoftSpace(f, 0);
        }
    }
    if (newline) {
        if (PyFile_WriteString("\n", f) < 0)
            return -1;
        PyFile_SoftSpace(f, 0);
    }
    return 0;
}

#else /* Python 3 has a print function */
static int __Pyx_Print(PyObject *arg_tuple, int newline) {
    PyObject* kwargs = 0;
    PyObject* result = 0;
    PyObject* end_string;
    if (!__pyx_print) {
        __pyx_print = PyObject_GetAttrString(__pyx_b, "print");
        if (!__pyx_print)
            return -1;
    }
    if (!newline) {
        if (!__pyx_print_kwargs) {
            __pyx_print_kwargs = PyDict_New();
            if (!__pyx_print_kwargs)
                return -1;
            end_string = PyUnicode_FromStringAndSize(" ", 1);
            if (!end_string)
                return -1;
            if (PyDict_SetItemString(__pyx_print_kwargs, "end", end_string) < 0) {
                Py_DECREF(end_string);
                return -1;
            }
            Py_DECREF(end_string);
        }
        kwargs = __pyx_print_kwargs;
    }
    result = PyObject_Call(__pyx_print, arg_tuple, kwargs);
    if (!result)
        return -1;
    Py_DECREF(result);
    return 0;
}
#endif

static PyObject *__Pyx_GetName(PyObject *dict, PyObject *name) {
    PyObject *result;
    result = PyObject_GetAttr(dict, name);
    if (!result)
        PyErr_SetObject(PyExc_NameError, name);
    return result;
}

static void __Pyx_Raise(PyObject *type, PyObject *value, PyObject *tb) {
    Py_XINCREF(type);
    Py_XINCREF(value);
    Py_XINCREF(tb);
    /* First, check the traceback argument, replacing None with NULL. */
    if (tb == Py_None) {
        Py_DECREF(tb);
        tb = 0;
    }
    else if (tb != NULL && !PyTraceBack_Check(tb)) {
        PyErr_SetString(PyExc_TypeError,
            "raise: arg 3 must be a traceback or None");
        goto raise_error;
    }
    /* Next, replace a missing value with None */
    if (value == NULL) {
        value = Py_None;
        Py_INCREF(value);
    }
    #if PY_VERSION_HEX < 0x02050000
    if (!PyClass_Check(type))
    #else
    if (!PyType_Check(type))
    #endif
    {
        /* Raising an instance.  The value should be a dummy. */
        if (value != Py_None) {
            PyErr_SetString(PyExc_TypeError,
                "instance exception may not have a separate value");
            goto raise_error;
        }
        /* Normalize to raise <class>, <instance> */
        Py_DECREF(value);
        value = type;
        #if PY_VERSION_HEX < 0x02050000
            if (PyInstance_Check(type)) {
                type = (PyObject*) ((PyInstanceObject*)type)->in_class;
                Py_INCREF(type);
            }
            else {
                type = 0;
                PyErr_SetString(PyExc_TypeError,
                    "raise: exception must be an old-style class or instance");
                goto raise_error;
            }
        #else
            type = (PyObject*) Py_TYPE(type);
            Py_INCREF(type);
            if (!PyType_IsSubtype((PyTypeObject *)type, (PyTypeObject *)PyExc_BaseException)) {
                PyErr_SetString(PyExc_TypeError,
                    "raise: exception class must be a subclass of BaseException");
                goto raise_error;
            }
        #endif
    }
    __Pyx_ErrRestore(type, value, tb);
    return;
raise_error:
    Py_XDECREF(value);
    Py_XDECREF(type);
    Py_XDECREF(tb);
    return;
}

static INLINE void __Pyx_ErrRestore(PyObject *type, PyObject *value, PyObject *tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    PyThreadState *tstate = PyThreadState_GET();

    tmp_type = tstate->curexc_type;
    tmp_value = tstate->curexc_value;
    tmp_tb = tstate->curexc_traceback;
    tstate->curexc_type = type;
    tstate->curexc_value = value;
    tstate->curexc_traceback = tb;
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
}

static INLINE void __Pyx_ErrFetch(PyObject **type, PyObject **value, PyObject **tb) {
    PyThreadState *tstate = PyThreadState_GET();
    *type = tstate->curexc_type;
    *value = tstate->curexc_value;
    *tb = tstate->curexc_traceback;

    tstate->curexc_type = 0;
    tstate->curexc_value = 0;
    tstate->curexc_traceback = 0;
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
        PyThreadState_GET(), /*PyThreadState *tstate,*/
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
