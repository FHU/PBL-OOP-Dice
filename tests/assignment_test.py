from pytest import mark
import pytest

import dice


def test_Die_instance_attributes():
    die = dice.Die()
    assert isinstance(die.value, int)
    assert isinstance(die.faces, int)


def test_Die_init():
    die = dice.Die(20)
    die2 = dice.Die()
    assert die.faces == 20
    assert die.value == 0
    assert die2.faces == 6


@mark.parametrize("faces", [1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 100, 1000])
def test_Die_roll_rng(faces):
    die = dice.Die(faces)
    for _ in range(10):
        roll = die.roll()
        assert 1 <= roll <= faces


@mark.parametrize("faces", [1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 100, 1000])
def test_Die_roll_update_value(faces):
    die = dice.Die(faces)
    roll = die.roll()
    assert roll == die.value


@mark.parametrize(
    "face, value", [(1, 1), (2, 2), (3, 2), (20, 7), (100, 82), (1000, 9)]
)
def test_Die_str(face, value):
    die = dice.Die()
    die.faces = face
    die.value = value
    assert str(die) == f"[d{face}] {value}"


def test_DiceSet_instance_attribute_blank():
    dice_set = dice.DiceSet()
    assert dice_set.dice == []


@mark.parametrize(
    "set", [[4], [5, 6], [3, 2, 9], [20, 7, 100, 20], [82, 25, 16, 6, 6, 6, 6, 6, 6]]
)
def test_DiceSet_instance_attribute_with_param(set):
    dice_set = dice.DiceSet(set)
    for i in range(len(set)):  # range(len(set))
        assert isinstance(dice_set.dice[i], dice.Die)


@mark.parametrize(
    "faces, values",
    [
        ([4], [2]),
        ([5, 6], [2, 1]),
        ([3, 2, 9], [1, 1, 9]),
        ([20, 7, 100, 20], [18, 4, 42, 8]),
    ],
)
def test_DiceSet_pop_die(faces, values):
    dice_set = dice.DiceSet(faces)
    for index, value in enumerate(values):
        dice_set.dice[index].value = value
    for value in values:
        die = dice_set.pop_die(value)
        assert die.value == value


def test_DiceSet_pop_die_error():
    dice_set = dice.DiceSet()
    with pytest.raises(AttributeError):
        dice_set.pop_die(4)


@mark.parametrize(
    "test_dice_set",
    [[4], [5, 6], [3, 2, 9], [20, 7, 100, 20], [82, 25, 16, 6, 6, 6, 6, 6, 6]],
)
def test_DiceSet_add_die(test_dice_set):
    dice_set = dice.DiceSet()
    for face in test_dice_set:
        dice_set.add_die(dice.Die(face))
    dice_set_faces = [die.faces for die in dice_set.dice]
    assert dice_set_faces == test_dice_set


@mark.parametrize(
    "set", [[4], [5, 6], [3, 2, 9], [20, 7, 100, 20], [82, 25, 16, 6, 6, 6, 6, 6, 6]]
)
def test_DiceSet_roll(set):
    calc_sum = 0
    dice_set = dice.DiceSet(set)
    sum = dice_set.roll()
    assert isinstance(sum, int)
    for die in dice_set.dice:
        calc_sum += die.value
    assert sum == calc_sum


def test_DiceSet_die_values():
    dice_set = dice.DiceSet([6, 6, 6, 6])
    dice_set.dice[0].value = 1
    dice_set.dice[1].value = 2
    dice_set.dice[2].value = 3
    dice_set.dice[3].value = 4
    assert 1 in dice_set.die_values()
    assert 2 in dice_set.die_values()
    assert 3 in dice_set.die_values()
    assert 4 in dice_set.die_values()


@mark.parametrize(
    "faces, values, dice_str",
    [
        ([4], [2], "{[d4] 2}"),
        ([5, 6], [2, 1], "{[d5] 2, [d6] 1}"),
        ([3, 2, 9], [1, 1, 9], "{[d3] 1, [d2] 1, [d9] 9}"),
        ([20, 7, 100, 20], [18, 4, 42, 8], "{[d20] 18, [d7] 4, [d100] 42, [d20] 8}"),
    ],
)
def test_DiceSet_str(faces, values, dice_str):
    dice_set = dice.DiceSet(faces)
    for index, value in enumerate(values):
        dice_set.dice[index].value = value
    assert str(dice_set) == dice_str
