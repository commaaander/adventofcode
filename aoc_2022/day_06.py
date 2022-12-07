""" https://adventofcode.com/2022/day/6
 """

from adventofcode import LOG

questions = [
    "How many characters need to be processed before the first start-of-packet marker is detected?",  # noqa: E501
    "How many characters need to be processed before the first start-of-message marker is detected?",  # noqa: E501
]


def part_one(**kwargs):
    LOG.debug(f"part_one({kwargs=})")
    answer = 0
    datastream_buffers = kwargs["raw_data"].split("\n")
    LOG.debug(f"{datastream_buffers=}")
    for datastream_buffer in datastream_buffers:
        LOG.debug(f"{datastream_buffer=}")
        for start_char in range(len(datastream_buffer)):
            test_sequence = datastream_buffer[start_char : start_char + 4]  # noqa: E203
            # LOG.debug(f"{datastream_buffer=}, {index=}, {test_sequence=}")
            if len(test_sequence) == len(set(test_sequence)):
                answer = start_char + 4
                LOG.debug(f"found: {test_sequence} at {answer}")
                break
    return questions[0], answer


def part_two(**kwargs):
    LOG.debug(f"part_two({kwargs=})")
    answer = 0
    datastream_buffers = kwargs["raw_data"].split("\n")
    LOG.debug(f"{datastream_buffers=}")
    for datastream_buffer in datastream_buffers:
        LOG.debug(f"{datastream_buffer=}")
        for start_char in range(len(datastream_buffer)):
            test_sequence = datastream_buffer[start_char : start_char + 14]  # noqa: E203
            # LOG.debug(f"{datastream_buffer=}, {index=}, {test_sequence=}")
            if len(test_sequence) == len(set(test_sequence)):
                answer = start_char + 14
                LOG.debug(f"found: {test_sequence} at {answer}")
                break
    return questions[1], answer
