from queue import Queue
lineup = Queue(maxsize=3)
lineup.get(block=False)
lineup.put("one")
lineup.put("two")
lineup.put("three")
lineup.put("four", timeout=1)
lineup.full()
lineup.get()
lineup.get()
lineup.get()
lineup.empty()
