-- Active: 1707069148322@@localhost@3306@punto_de_venta_uvm
CREATE TABLE unidades (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(30) NOT NULL UNIQUE
);

CREATE TABLE categorias (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(30) NOT NULL UNIQUE
);

CREATE TABLE marcas (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(30) NOT NULL UNIQUE
);

CREATE TABLE productos (
  sku INT AUTO_INCREMENT PRIMARY KEY,
  unidad_id INT NOT NULL,
  categoria_id INT NOT NULL,
  marca_id INT NOT NULL,
  cantidad INT NOT NULL CHECK (cantidad >= 0),
  precio_compra DECIMAL(10, 2) NOT NULL CHECK (precio_compra >= 0),
  precio_venta DECIMAL(10, 2) NOT NULL CHECK (precio_venta >= 0),
  stock_minimo INT NOT NULL DEFAULT 1 CHECK (stock_minimo >= 0),
  FOREIGN KEY (unidad_id) REFERENCES unidades(id) ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (categoria_id) REFERENCES categorias(id) ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (marca_id) REFERENCES marcas(id) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE proveedores (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(30) NOT NULL UNIQUE,
  telefono CHAR(10) NOT NULL UNIQUE
);

CREATE TABLE compras (
  id INT AUTO_INCREMENT PRIMARY KEY,
  proveedor_id INT NOT NULL,
  fecha DATE NOT NULL,
  total DECIMAL(10, 2) NOT NULL CHECK (total >= 0),
  FOREIGN KEY (proveedor_id) REFERENCES proveedores(id) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE detalle_compra (
  compra_id INT NOT NULL,
  producto_id INT NOT NULL,
  cantidad INT NOT NULL CHECK (cantidad > 0),
  precio_compra_unitario DECIMAL(10, 2) NOT NULL CHECK (precio_compra_unitario >= 0),
  total_unitario DECIMAL(10, 2) NOT NULL CHECK (total_unitario >= 0),
  PRIMARY KEY (compra_id, producto_id),
  FOREIGN KEY (compra_id) REFERENCES compras(id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (producto_id) REFERENCES productos(sku) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE clientes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre_completo VARCHAR(50) NOT NULL,
  edad INT CHECK (edad >= 18),
  correo VARCHAR(50) NOT NULL UNIQUE,
);

CREATE TABLE ventas (
  id INT AUTO_INCREMENT PRIMARY KEY,
  cliente_id INT NOT NULL,
  fecha DATE NOT NULL,
  total DECIMAL(5, 2) NOT NULL CHECK (total >= 0),
  FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE detalle_venta (
  venta_id INT NOT NULL,
  producto_id INT NOT NULL,
  cantidad INT NOT NULL CHECK (cantidad > 0),
  precio_venta_unitario DECIMAL(4, 2) NOT NULL CHECK (precio_venta_unitario >= 0),
  total_unitario DECIMAL(5, 2) NOT NULL CHECK (total_unitario >= 0),
  PRIMARY KEY (venta_id, producto_id),
  FOREIGN KEY (venta_id) REFERENCES ventas(id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (producto_id) REFERENCES productos(sku) ON DELETE RESTRICT ON UPDATE CASCADE
);