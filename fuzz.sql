drop database if exists fuzz_png;
create database fuzz_png;

use fuzz_png;

drop table if exists filename;

create table filename(
    `id` int(10) UNIQUE NOT NULL auto_increment,
    `name` varchar(24) NOT NULL,
    `staus` int(1) NOT NULL,
    PRIMARY KEY(`id`)
)ENGINE=InnoDB default CHARSET=utf8;