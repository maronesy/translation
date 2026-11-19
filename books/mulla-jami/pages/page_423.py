# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 423 (printed ٤٢٢)."""

PAGE_NUMBER = 423
PRINTED_PAGE = "٤٢٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «والأعلام الغالبة التي تعينت لفرد معين بغلبة» at the foot of PDF p. 422.
    {"type": "matn",
     "ar": "الاستعمال فيه داخلة في التعريف؛ لأن غلبة استعمال المستعملين بحيث اختص العلم الغالب بفرد معين بمنزلة الوضع من واضع معين، فكأن هؤلاء المستعملين وضعوا له ذلك",
     "en": "…of usage are included in the definition; for the predominance of the users’ usage, such that the predominant proper name has become restricted to a specific individual, is equivalent to imposition by a specific imposer, as if those users had imposed that [name] for it."},
    {"type": "matn",
     "ar": "(غير متناول غيره) أي: حال كون ذلك الاسم الموضوع لشيء بعينه غير متناول غير ذلك الشيء باستعماله فيه.",
     "en": "(Not covering anything else), that is, that noun imposed for a thing in its very identity being such that it does not cover anything other than that thing by being used for it."},
    {"type": "matn",
     "ar": "واحترز به عن المعارف كلها[[١]].",
     "en": "By this he excludes all the [other] definite nouns."},
    {"type": "matn",
     "ar": "وقوله: (بوضع واحد) أي: تناولا بوضع واحد[[٢]]؛ لئلا يخرج الأعلام المشتركة[[٣]].",
     "en": "His words (by a single imposition) mean: covering by a single imposition; so that homonymous proper names (al-aʿlām al-mushtaraka) are not excluded."},
    {"type": "matn",
     "ar": "ولما أشار إلى ترتيب أنواع المعارف في الأعرفية بترتيبها في الذكر أراد التنبيه على ترتيب أصنافها فيما يكون[[٤]] فيه هذا الترتيب[[٥]]، فقال:",
     "en": "Having indicated the ranking of the kinds of definite nouns in degree of definiteness (aʿrafiyya) by the order in which he mentioned them, he wished to draw attention to the ranking of their sub-classes in those [kinds] in which this ranking exists, and so he said:"},
    {"type": "matn",
     "ar": "(وأعرفها) أي: أعرف المعارف، يعني: أقلها لبسا عند المخاطب من حيث أصنافها (المضمر المتكلم) لبعد وقوع الالتباس فيه.",
     "en": "(And the most definite of them), that is, the most definite of the definite nouns—meaning the least liable to confusion for the addressee with respect to their sub-classes—(is the first-person pronoun), because confusion is unlikely to occur in it."},
    {"type": "matn",
     "ar": "(ثم) المضمر (المخاطب[[٦]]) فإنه يتطرق فيه ما لا يتطرق في المتكلم،",
     "en": "(Then) the (second-person) pronoun, for there enters into it what does not enter into the first person."},
    {"type": "matn",
     "ar": "ألا ترى أنك إذا قلت: «أنا» لم يلتبس بغيره، وإذا قلت: «أنت» جاز أن يلتبس بآخر، فيتوهم أن الخطاب له،",
     "en": "Do you not see that when you say “anā” (I), it is not confused with anyone else, whereas when you say “anta” (you), it may be confused with another, so that it is imagined that the address is to him?"},
    {"type": "matn",
     "ar": "وليس المراد بالأعرفية إلا كون المعرفة أبعد من اللبس.",
     "en": "What is meant by greater definiteness is nothing but the definite noun’s being further from confusion."},
    {"type": "matn",
     "ar": "ثم المضمر الغائب، ولم يذكره؛ لأنه علم من أعرفية المتكلم والمخاطب أنه أدون",
     "en": "Then the third-person pronoun. He did not mention it because it is known from the greater definiteness of the first and second persons that it is lower…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لو قال: ما وضع بوضع واحد لشيء واحد بعينه لكان أخصر وأوضح.",
     "en": "Had he said “what is imposed by a single imposition for a single thing in its very identity”, it would have been more concise and clearer."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "إشارة إلى أن قوله: بوضع واحد ظرف لغو متعلق بالمنفي، أعني: متناولا لا بالنفي المستفاد من غير، فيكون داخلا تحت المنفي، فيفيد عموم التعريف للأعلام المشتركة،",
     "en": "[This is] an indication that his words “by a single imposition” are a dependent adverbial (ẓarf laghw) attached to what is negated, namely “covering”, not to the negation conveyed by ghayr; so it falls under what is negated, and thereby the definition extends to homonymous proper names."},
    {"type": "pair",
     "ar": "وليس مقصوده أنه مفعول مطلق بتقدير «تناولا» على ما وهم؛ إذ لا حاجة إليه على أنه بعد تقدير تناولا متعلق به، فليكن أول الأمر متعلقا بمتناولا.",
     "en": "His purpose is not that it is an absolute object with “tanāwulan” understood, as has been wrongly supposed; for there is no need for that, and moreover, after supposing “tanāwulan”, it is attached to it—so let it be attached from the outset to “mutanāwilan”."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لا تقول قد خرج بقوله: غير متناول غيره الأعلام المشتركة، فقوله: بوضع واحد ليدخل لا لئلا يخرج؛",
     "en": "Do not say: homonymous proper names were already excluded by his words “not covering anything else”, so his words “by a single imposition” serve to include [them], not to prevent their exclusion;"},
    {"type": "pair",
     "ar": "لأنا نقول: ليس المذكور في الحد عدم التناول المطلق بل المقيد، فلا يخرج به الأعلام المشتركة، فافهم.",
     "en": "for we say: what is mentioned in the definition is not the absence of covering absolutely but of [covering] qualified [by a single imposition], so homonymous proper names are not excluded by it. So understand."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: في نوع يكون فيه هذا الترتيب أي: ترتيب الأصناف في نفسها؛ لأن المضاف يكون فيه هذا الترتيب.",
     "en": "That is, in a kind in which this ranking exists, that is, the ranking of the sub-classes among themselves; for in the annexed noun this ranking exists."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "يشعر بأنه لا ترتيب فيما بين أصناف المبهمات، وقد عرفت أن اسم الإشارة أعرف من الموصول،",
     "en": "This suggests that there is no ranking among the sub-classes of the vague nouns, whereas you have learned that the demonstrative noun is more definite than the relative noun;"},
    {"type": "pair",
     "ar": "وبأنه لا ترتيب فيما بين أصناف المضاف إلى أحدها معنى، وتعريف المضاف بحسب تعريف المضاف إليه،",
     "en": "and that there is no ranking among the sub-classes of what is annexed to one of them in meaning, whereas the definiteness of the annexed noun accords with the definiteness of the noun to which it is annexed."},
    {"type": "pair",
     "ar": "فالأولى أن يقول: أراد التنبيه على ترتيب أصنافها فيما يكون فيه هذا الترتيب، ويحتاج إلى التنبيه.",
     "en": "So it would be better to say: he wished to draw attention to the ranking of their sub-classes in those [kinds] in which this ranking exists and which need to be pointed out."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "ليس وجه كون المضمر المخاطب أعرف من النداء ظاهرا إلا أن يجعل تعريفه لكونه في الأصل معرفا باللام.",
     "en": "The reason why the second-person pronoun is more definite than the vocative is not evident—unless its [the vocative’s] definiteness is held to be due to its having originally been made definite by the lām."},
]
