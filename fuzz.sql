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


drop table if exists process;

create table process(
    `id` int(2) UNIQUE NOT NULL auto_increment,
    `py` int(1) NOT NULL,
    `js` int(1) NOT NULL
)ENGINE=InnoDB default CHARSET=utf8;

insert into process(`py`,`js`) values(1,1);