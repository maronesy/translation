# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 239 (printed ٢٣٨)."""

PAGE_NUMBER = 239
PRINTED_PAGE = "٢٣٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(ولا تقول) في المثال الأول: («إياك الأسد»[[١]]؛ لامتناع تقدير «من») وشذوذه من غير «أن وأن».",
     "en": "(And you do not say) in the first example: (“iyyāka al-asada,” because supplying “min” is excluded), it being anomalous with anything other than “anna” and “an.”"},
    {"type": "matn",
     "ar": "فإن قلت: فليكن بتقدير العاطف؟",
     "en": "If you say: then let it be with the conjunction (al-ʿāṭif) supplied?"},
    {"type": "matn",
     "ar": "قلنا: حذف العاطف أشد شذوذا؛ لأن حذف حرف الجر قياس مع «أن وأن»، شاذ كثير في غيرهما. وأما حذف العاطف، فلم يثبت إلا نادرا.",
     "en": "We say: eliding the conjunction is more anomalous still; for eliding the preposition is regular with “anna” and “an,” and anomalous yet frequent with others; whereas eliding the conjunction is attested only rarely."},

    {"type": "section", "ar": "[المفعول فيه]",
     "en": "The Adverbial of Time and Place (al-Mafʿūl fīhi)"},

    {"type": "matn",
     "ar": "(المفعول فيه[[٢]]: هو ما فعل فيه[[٣]] فعل) أي: حدث[[٤]] (مذكور[[٥]]) تضمنا[[٦]] في ضمن الفعل الملفوظ أو المقدر أو شبهه كذلك، أو مطابقة إذا كان العامل مصدرا[[٧]].",
     "en": "(The mafʿūl fīhi [adverbial of time and place] is that in which an action is done), that is, an event, (that is mentioned)—by implication (taḍammunan), within the uttered or implied verb or what resembles it likewise, or by direct correspondence (muṭābaqatan) when the governor is a maṣdar."},
    {"type": "matn",
     "ar": "فقوله: «ما فعل فيه فعل» شامل لأسماء الزمان والمكان[[٨]] كلها، فإنه لا يخلو زمان أو مكان عن أن يفعل فيهما[[٩]] فعل سواء ذكر الفعل الذي فعل فيهما أو لا[[١٠]].",
     "en": "So his words “that in which an action is done” include all nouns of time and place; for no time or place is free of an action being done in them, whether the action done in them is mentioned or not."},
    {"type": "matn",
     "ar": "وقوله: «مذكور» خرج به ما لا يذكر فعل فعل فيه نحو: «يوم الجمعة يوم طيب»، فإنه وإن كان فعل فيه فعل لا محالة، لكنه ليس بمذكور،",
     "en": "His words “mentioned” exclude that for which no action done in it is mentioned, as in “Friday is a good day”; for although some action is inevitably done in it, it is not mentioned."},
    {"type": "matn",
     "ar": "ولكن بقي مثل: «شهدت يوم الجمعة» داخلا فيه، فإن «يوم الجمعة» يصدق عليه أنه فعل فيه فعل مذكور؛ فإن شهود يوم الجمعة لا يكون إلا يوم الجمعة،",
     "en": "But something like “I witnessed Friday” still remains included in it, since it is true of “Friday” that a mentioned action was done in it; for witnessing Friday takes place only on Friday."},
    {"type": "matn",
     "ar": "فلو اعتبر في التعريف قيد الحيثية أي: المفعول فيه: «ما فعل فيه فعل مذكور من حيث إنه فعل فيه فعل مذكور» لخرج مثل هذا المثال",
     "en": "Had the qualification of respect (qayd al-ḥaythiyya) been taken into account in the definition—that is, the mafʿūl fīhi is “that in which a mentioned action is done, inasmuch as a mentioned action is done in it”—an example like this would be excluded…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أما قول الشاعر: «فإياك إياك المراء فإنه» فلضرورة الشعر، أو لأن إياك إياك من باب الأسد الأسد.",
     "en": "As for the poet’s words “So beware, beware of disputation (al-mirāʾ), for it…,” it is by poetic licence; or because “iyyāka iyyāka” belongs to the type of “al-asada al-asada.”"},
    {"type": "pair",
     "ar": "والمراء منصوب بمثل «اترك» أو «احذر»، أو لأن المراء في تأويل أن تمارى.",
     "en": "Then “al-mirāʾ” is in the accusative by something like “utruk” (leave) or “iḥdhar” (beware); or because “al-mirāʾ” is interpreted as “an tumārā” (that you dispute)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: ومنه المفعول فيه، أو هذا باب المفعول فيه، أو المفعول فيه هو كذا.",
     "en": "That is: “and among them is the mafʿūl fīhi,” or “this is the chapter of the mafʿūl fīhi,” or “the mafʿūl fīhi is such-and-such.”"},
    {"type": "pair",
     "ar": "وهو فصل على الأخير، وصدر استئنافية على الأولين.",
     "en": "On the last [reading] it is a separating pronoun (faṣl); on the first two, it begins a new (istiʾnāfiyya) sentence."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: في مسماه، أو في نفسه مسامحة، أو اسم ما فعل فيه.",
     "en": "That is: in what it names; or “in it” itself, by loose usage; or [the meaning is] the noun of that in which [an action] is done."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "وهو الفعل اللغوي.",
     "en": "That is, the action in the lexical sense (al-fiʿl al-lughawī)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: مؤدى.",
     "en": "That is: expressed."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "إلى قوله: «أو مطابقة» كأنه أراد بالمطابقة الدلالة على المقصود بالأصالة، وبالتضمن ما يقابلها،",
     "en": "[From “taḍammunan”] up to his words “or by direct correspondence”: it is as though by direct correspondence (muṭābaqa) he meant signifying what is primarily intended, and by implication (taḍammun) its counterpart;"},
    {"type": "pair",
     "ar": "فيندرج في المذكور المستعمل في المعنى الالتزامي وما له لمح إلى معنى.",
     "en": "so under “mentioned” falls [a word] used in an entailed (iltizāmī) sense and one that has an allusion to a meaning."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أو ما بمعناه بأن يكون اسم المصدر.",
     "en": "Or what has its meaning, by being a noun of the maṣdar (ism al-maṣdar)."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "المراد باسم الزمان المعنى الإضافي لا المفهوم الاصطلاحي، وهو ظاهر.",
     "en": "What is meant by “noun of time” is the compositional sense, not the technical concept; and this is evident."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "صوابه: فيه.",
     "en": "Correctly: “fīhi” (in it)."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "لفظا أو تقديرا، وهو المراد بالذكر، والمذكور في هذا البحث فلا تغفل.",
     "en": "Explicitly or by implication; that is what is meant by “mention” and “mentioned” in this discussion, so do not overlook it."},
]
