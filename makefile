default:
	# python2 -m buildozer
	# adb shell input keyevent KEYCODE_WAKEUP
	# @echo "Built and deployed"
	echo -e '#!/usr/bin/sh\npython2 main.py' > main.py.out
	chmod +x ./main.py.out
mdkvfile.kv.out: default
main.py.out: default
# out: main.py mdkvfile.kv buildozer.spec
# 	python2 -m buildozer
# 	adb shell input keyevent KEYCODE_WAKEUP
# main.py.out: main.py mdkvfile.kv buildozer.spec
# 	python2 -m buildozer
	# adb shell input keyevent KEYCODE_WAKEUP
	# cp main.py main.py.out
	# chmod +x main.py.out
%.c.out: %.c
	gcc -g -o $@ $< -lrt -lreadline
clean:
	rm -rf *.out
%.py.out: %.py
	cp $< $@
	chmod +x $@
%.pl.out: %.pl
	cp $< $@
	chmod +x $@
%.sh.out: %.sh
	cp $< $@
	chmod +x $@
%.s.out: %.o
	arm-none-eabi-ld -o $@ $<
%.o: %.s
	arm-none-eabi-as -g -o $<.o
%.m.out: %.m
	cp $< $@
	chmod +x $@
