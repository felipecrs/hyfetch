
from hyfetch.distro import AsciiArt

container_linux_by_coreos = AsciiArt(match=r'''"Container Linux by CoreOS"* | "Container_Linux"*''', color='4 7 1', ascii=r"""
${c1}                .....
          .';:cccccccc:;'.
        ':ccccclc${c3}lllllllll${c1}cc:.
     .;cccccccc${c3}lllllllllllllll${c1}c,
    ;clllccccc${c3}llllllllllllllllll${c1}c,
  .cllclccccc${c3}lllll${c2}lll${c3}llllllllllll${c1}c:
  ccclclcccc${c3}cllll${c2}kWMMNKk${c3}llllllllll${c1}c:
 :ccclclcccc${c3}llll${c2}oWMMMMMMWO${c3}lllllllll${c1}c,
.ccllllllccc${c3}clll${c2}OMMMMMMMMM0${c3}lllllllll${c1}c
.lllllclcccc${c3}llll${c2}KMMMMMMMMMMo${c3}llllllll${c1}c.
.lllllllcccc${c3}clll${c2}KMMMMMMMMN0${c3}lllllllll${c1}c.
.cclllllcccc${c3}lllld${c2}xkkxxdo${c3}llllllllllc${c1}lc
 :cccllllllcccc${c3}lllccllllcclccc${c1}cccccc;
 .ccclllllllcccccccc${c3}lll${c1}ccccclccccccc
  .cllllllllllclcccclccclccllllcllc
    :cllllllllccclcllllllllllllcc;
     .cccccccccccccclcccccccccc:.
       .;cccclccccccllllllccc,.
          .';ccccclllccc:;..
                .....
""")
    