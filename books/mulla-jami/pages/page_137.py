# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 137 (printed ١٣٦)."""

PAGE_NUMBER = 137
PRINTED_PAGE = "١٣٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "الحصر المطلوب، فلا يجب تقديم الفاعل، لكن لم يستحسنه بعضهم؛ لأنه من قبيل قصر الصفة على شيء قبل تمامها[[١]].",
     "en": "…the intended restriction (ḥaṣr); so fronting the agent (fāʿil) is not obligatory, though some scholars did not deem it commendable, because it belongs to the category of confining an attribute to something before its completion."},
    {"type": "matn",
     "ar": "وإنما قلنا: «الظاهر أن معناه كذا» لاحتمال أن يكون معناه: «ما ضرب أحدا أحد إلا عمرا زيد»[[٢]]، فيفيد انحصار صفة كل واحد منهما في الآخر، وهو أيضا خلاف المقصود.",
     "en": "We said only “the apparent sense is such-and-such” because it may possibly mean: “No one struck anyone save that ʿAmr [was struck by] Zayd,” which would yield the mutual confinement of each one’s attribute to the other — and this too is contrary to what is intended."},
    {"type": "matn",
     "ar": "وأما وجوب تقديمه عليه في صورة وقوع المفعول بعد معنى «إلا»؛ لأن الحصر ههنا في الجزء الأخير، فلو أخر الفاعل انقلب المعنى قطعا.",
     "en": "As for the obligatory fronting of it (the object) over it (the agent) in the case where the object falls after the sense of “illā”: it is because the restriction here lies in the last part, so were the agent postposed the meaning would be inverted, decisively."},

    {"type": "section", "ar": "[ تأخير الفاعل عن المفعول ]",
     "en": "Postposing the Agent after the Object"},

    {"type": "matn",
     "ar": "(وإذا اتصل به)[[٣]] أي: بالفاعل: ١-(ضمير مفعول) نحو: «ضرب زيدا غلامه».",
     "en": "His words “And when there is joined to it” — that is, to the agent — [there falls]: (1) the pronoun of an object, as in “His servant struck Zayd” (ḍaraba Zaydan ghulāmuhu)."},
    {"type": "matn",
     "ar": "٢-(أو وقع) أي: الفاعل (بعد «إلا») المتوسطة بينهما في صورتي التقديم والتأخير، نحو: «ما ضرب عمرا إلا زيد»، وفائدة هذا القيد مثل ما عرفت آنفا.",
     "en": "(2) “Or it falls” — that is, the agent — “after ‘illā’” that stands between the two in both the fronted and postposed configurations, as in “None struck ʿAmr but Zayd”; and the benefit of this restriction is like what you learned just now."},
    {"type": "matn",
     "ar": "٣-(أو) وقع الفاعل بعد (معناها) أي: معنى «إلا»، نحو: «إنما ضرب عمرا زيد».",
     "en": "(3) “Or” the agent falls after “its meaning” — that is, the meaning of “illā” — as in “Only Zayd struck ʿAmr” (innamā ḍaraba ʿAmran Zaydun)."},
    {"type": "matn",
     "ar": "٤-(أو اتصل مفعوله) بأن يكون المفعول ضميرا متصلا بالفعل[[٤]] (وهو) أي: الفاعل (غير) ضمير (متصل به) نحو: «ضربك زيد» (وجب تأخيره)[[٥]] أي: تأخير الفاعل عن المفعول في جميع هذه الصور.",
     "en": "(4) “Or its object is joined [to the verb]” — such that the object is a pronoun affixed to the verb — “while it” — that is, the agent — “is not a pronoun affixed to it,” as in “Zayd struck you” (ḍarabaka Zaydun): then “its postposing becomes obligatory” — that is, postposing the agent after the object in all of these cases."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ففيه عدول عن الأصل مع منع مانع عن العدول، ولا يجوز العدول بلا منع مانع عن الأصل فضلا عن جوازه مع المانع عن العدول.",
     "en": "For in it there is a departure from the default while there is an impediment barring that departure; and departure from the default is not permissible when nothing bars it, let alone its being permissible when there is an impediment against the departure."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "كما ذهب إليه جماعة من النحويين. وأما عند أكثرهم فلا يجوز استثناء شيئين بأداة واحدة بلا عطف،",
     "en": "As a group of the grammarians held. But according to most of them, excepting two things by a single instrument without a conjunction is not permissible;"},
    {"type": "pair",
     "ar": "وللمجوزين أن يستدلوا بقوله تعالى: ﴿وما نراك اتبعك إلا الذين هم أراذلنا بادي الرأي﴾ (سورة هود:٢٧)، أي: وما نراك اتبعك أحد في حال من الأحوال إلا الذين هم أراذلنا في بادئ الرأي، أي: بلا رواية قوية،",
     "en": "Those who permit it may adduce as evidence His words, the Exalted: “And we do not see anyone following you except those who are the lowliest among us, at first glance” (Qurʾān, Sūrat Hūd 11:27) — meaning: we do not see that anyone has followed you in any state whatever except those who are our lowliest, at first glance — that is, without any firm transmission;"},
    {"type": "pair",
     "ar": "وقد يرد بأن الظرف متعلق بفعل مقدر، أي: اتبعوا في بادئ الرأي، أو بأن الظرف مما يكفيه رائحة من الفعل.",
     "en": "It may be countered that the adverbial phrase is governed by an implied verb — i.e., “they followed at first glance” — or that the adverbial phrase is of the kind for which a mere whiff of the verb suffices."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وكذا إذا اتصل بصلة أو صفة ضمير المفعول عند من لم يجوز الفصل بين الصفة والموصوف بالأجنبي، نحو: «ضرب زيدا الذي ضرب غلامه» و«أكرم هندا رجل ضرب غلامها».",
     "en": "Likewise when the object-pronoun is joined to a relative clause (ṣila) or an adjective, according to one who does not permit separating the adjective from its qualified noun by an extraneous element, as in “The one who struck his servant struck Zayd,” and “A man who struck her servant honored Hind.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "بقي فيه نحو: «زيد ضربك»، فإن المفعول فيه ضمير متصل بالفعل، مع أنه يجب تقديم الفاعل، فأخرجه بقوله: «وهو غير متصل».",
     "en": "There remains within it a case like “Zayd struck you,” for the object in it is a pronoun affixed to the verb, yet fronting the agent is there obligatory; so he excluded it by his words “while it is not affixed.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لم يقل: وجب تقديمه، أي: المفعول؛ لأنه ذاكر أحوال الفاعل.",
     "en": "He did not say “its fronting becomes obligatory” — meaning the object’s — because he is here enumerating the states of the agent."},
]
