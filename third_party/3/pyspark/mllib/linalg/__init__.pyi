# Stubs for pyspark.mllib.linalg (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from pyspark.ml import linalg as newlinalg
from pyspark.sql.types import UserDefinedType

class VectorUDT(UserDefinedType):
    @classmethod
    def sqlType(cls): ...
    @classmethod
    def module(cls): ...
    @classmethod
    def scalaUDT(cls): ...
    def serialize(self, obj): ...
    def deserialize(self, datum): ...
    def simpleString(self): ...

class MatrixUDT(UserDefinedType):
    @classmethod
    def sqlType(cls): ...
    @classmethod
    def module(cls): ...
    @classmethod
    def scalaUDT(cls): ...
    def serialize(self, obj): ...
    def deserialize(self, datum): ...
    def simpleString(self): ...

class Vector:
    __UDT__ = ...  # type: Any
    def toArray(self): ...
    def asML(self): ...

class DenseVector(Vector):
    array = ...  # type: Any
    def __init__(self, ar) -> None: ...
    @staticmethod
    def parse(s): ...
    def __reduce__(self): ...
    def numNonzeros(self): ...
    def norm(self, p): ...
    def dot(self, other): ...
    def squared_distance(self, other): ...
    def toArray(self): ...
    def asML(self): ...
    @property
    def values(self): ...
    def __getitem__(self, item): ...
    def __len__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self): ...
    def __getattr__(self, item): ...
    __neg__ = ...  # type: Any
    __add__ = ...  # type: Any
    __sub__ = ...  # type: Any
    __mul__ = ...  # type: Any
    __div__ = ...  # type: Any
    __truediv__ = ...  # type: Any
    __mod__ = ...  # type: Any
    __radd__ = ...  # type: Any
    __rsub__ = ...  # type: Any
    __rmul__ = ...  # type: Any
    __rdiv__ = ...  # type: Any
    __rtruediv__ = ...  # type: Any
    __rmod__ = ...  # type: Any

class SparseVector(Vector):
    size = ...  # type: Any
    indices = ...  # type: Any
    values = ...  # type: Any
    def __init__(self, size, *args) -> None: ...
    def numNonzeros(self): ...
    def norm(self, p): ...
    def __reduce__(self): ...
    @staticmethod
    def parse(s): ...
    def dot(self, other): ...
    def squared_distance(self, other): ...
    def toArray(self): ...
    def asML(self): ...
    def __len__(self): ...
    def __eq__(self, other): ...
    def __getitem__(self, index): ...
    def __ne__(self, other): ...
    def __hash__(self): ...

class Vectors:
    @staticmethod
    def sparse(size, *args): ...
    @staticmethod
    def dense(*elements): ...
    @staticmethod
    def fromML(vec): ...
    @staticmethod
    def stringify(vector): ...
    @staticmethod
    def squared_distance(v1, v2): ...
    @staticmethod
    def norm(vector, p): ...
    @staticmethod
    def parse(s): ...
    @staticmethod
    def zeros(size): ...

class Matrix:
    __UDT__ = ...  # type: Any
    numRows = ...  # type: Any
    numCols = ...  # type: Any
    isTransposed = ...  # type: Any
    def __init__(self, numRows, numCols, isTransposed: bool = ...) -> None: ...
    def toArray(self): ...
    def asML(self): ...

class DenseMatrix(Matrix):
    values = ...  # type: Any
    def __init__(self, numRows, numCols, values, isTransposed: bool = ...) -> None: ...
    def __reduce__(self): ...
    def toArray(self): ...
    def toSparse(self): ...
    def asML(self): ...
    def __getitem__(self, indices): ...
    def __eq__(self, other): ...

class SparseMatrix(Matrix):
    colPtrs = ...  # type: Any
    rowIndices = ...  # type: Any
    values = ...  # type: Any
    def __init__(self, numRows, numCols, colPtrs, rowIndices, values, isTransposed: bool = ...) -> None: ...
    def __reduce__(self): ...
    def __getitem__(self, indices): ...
    def toArray(self): ...
    def toDense(self): ...
    def asML(self): ...
    def __eq__(self, other): ...

class Matrices:
    @staticmethod
    def dense(numRows, numCols, values): ...
    @staticmethod
    def sparse(numRows, numCols, colPtrs, rowIndices, values): ...
    @staticmethod
    def fromML(mat): ...

class QRDecomposition:
    def __init__(self, Q, R) -> None: ...
    @property
    def Q(self): ...
    @property
    def R(self): ...