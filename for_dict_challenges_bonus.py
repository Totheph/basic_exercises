#вроде сделала 4 первые пункта (как же это было тяжело :((( ))))
#пятый пункт в процессе, сдам его потом


import random
import uuid
import datetime

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids, random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


def more_messages(users_list):
    ids = [user["sent_by"] for user in users_list]
    return max(set(ids), key=ids.count)

def more_answers(users_list):
    ids_list = {}
    all_reply = [message["reply_for"] for message in users_list]
    for message in users_list:
        for reply in all_reply:
            if reply == message["id"]:
                ids_list[message["sent_by"]]= ids_list.get(message['sent_by'], 0) + 1
    return max(ids_list, key=ids_list.get)

def most_seen_users(messages_list):
    views_list = {}
    for message in messages_list:
        total_views = views_list.get(message["sent_by"], [])
        total_views.extend(message["seen_by"])
        views_list[message["sent_by"]] = total_views
    for key, value in views_list.items():
        value = list(set(value))
        views_list[key] = value
    m = max(views_list.values(), key = len)
    users_max_views = []
    for key, value in views_list.items():
        if value == m:
            users_max_views.append(key)
    return users_max_views

def more_time(messages_list):
    time_dict = {}
    for message in messages_list:
        if datetime.time(0, 0, 0) < message["sent_at"].time() < datetime.time(12, 0, 0):
            time_dict["утро"] = time_dict.get("утро", 0) + 1
        elif datetime.time(12, 0, 0) <= message["sent_at"].time() <= datetime.time(18, 0, 0):
            time_dict["день"] = time_dict.get("день", 0) + 1
        else:
            time_dict["вечер"] = time_dict.get("вечер", 0) + 1
    return max(time_dict, key=time_dict.get)


def main():
    messages = generate_chat_history()
    print(f"ID пользователя, отправившего больше всего сообщений: {more_messages(messages)}")
    print(f"ID пользователя, на сообщения которого отвечали больше всего: {more_answers(messages)}")
    print("Больше просмотров у пользователей:", *more_views(messages))
    print(f"Больше всего сообщений было отправлено в {more_time(messages)}")
    

if __name__ == "__main__":
    main()
