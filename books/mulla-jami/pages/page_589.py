# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 589 (printed ٥٨٨)."""

PAGE_NUMBER = 589
PRINTED_PAGE = "٥٨٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Begins a new sentence after the end of PDF p. 588.
    {"type": "matn",
     "ar": "(وتقدير القسم كاللفظ) أي: كالتلفظ به، أو مقدره كملفوظه في صدر الكلام،",
     "en": "(And the supposition of an oath is like its explicit wording), that is, like uttering it; or, an oath supposed at the head of the speech is like one uttered,"},
    {"type": "matn",
     "ar": "فلزم في الشرط الذي بعده المضي وكان الجواب للقسم",
     "en": "so the perfect is required in the condition that follows it, and the apodosis belongs to the oath,"},
    {"type": "matn",
     "ar": "(نحو) قوله تعالى: (﴿لئن أخرجوا لا يخرجون﴾[[١]]) أي: «والله لئن أخرجوا»،",
     "en": "(as in) His words, the Exalted: (“If they are expelled, they will not go out”), that is, “by Allah, if they are expelled”;"},
    {"type": "matn",
     "ar": "فالشرط ماض، و«لا يخرجون» جواب القسم، فإنه لو كان جزاء الشرط لكان الجزم بحذف النون أولى به، أي: لا يخرجوا.",
     "en": "so the condition is a perfect, and “lā yakhrujūna” is the apodosis of the oath; for were it the apodosis (jazāʾ) of the condition, the jussive by dropping the nūn would have been more fitting for it, that is, “lā yakhrujū”."},
    {"type": "matn",
     "ar": "(و) كذا قوله تعالى: (﴿وإن أطعتموهم إنكم لمشركون﴾[[٢]]) أي: «والله إن أطعتموهم إنكم لمشركون»،",
     "en": "(And) likewise His words, the Exalted: (“And if you obey them, you are indeed polytheists”), that is, “by Allah, if you obey them, you are indeed polytheists”;"},
    {"type": "matn",
     "ar": "فالشرط ماض، و«إنكم لمشركون» جواب القسم، فإنه لو كان جزاء الشرط يلزم الإتيان بالفاء؛ لأن الجملة الاسمية الواقعة جزاء يجب فيها الفاء.",
     "en": "so the condition is a perfect, and “innakum la-mushrikūna” is the apodosis of the oath; for were it the apodosis of the condition, the fāʾ would have to be supplied, since a nominal sentence occurring as apodosis requires the fāʾ."},
    {"type": "matn",
     "ar": "(و«أما» للتفصيل) أي: تفصيل ما أجمله المتكلم في الذكر،",
     "en": "(And “ammā” is for detailing (tafṣīl)), that is, for detailing what the speaker has stated in summary form in what he mentioned,"},
    {"type": "matn",
     "ar": "نحو قولك: «جاءني إخوتك؛ أما زيد فأكرمته، وأما عمرو فأهنته، وأما بشر فأعرضت عنه»",
     "en": "as in your saying: “your brothers came to me; as for Zayd, I honoured him; as for ʿAmr, I insulted him; and as for Bishr, I turned away from him”;"},
    {"type": "matn",
     "ar": "أو ما أجمله في الذهن ويكون معلوما للمخاطب بواسطة القرائن،",
     "en": "or what he has held in summary form in the mind, which is known to the addressee by means of contextual indications (qarāʾin)."},
    {"type": "matn",
     "ar": "وقد جاءت للاستئناف من غير أن يتقدمها إجمال، نحو «أما» الواقعة في أوائل الكتب،",
     "en": "It sometimes comes to begin anew (istiʾnāf) without any summary preceding it, as with the “ammā” that occurs at the beginnings of books."},
    {"type": "matn",
     "ar": "ومتى كانت لتفصيل المجمل وجب تكرارها، وقد يكتفى بذكر قسم واحد، حيث يكون المذكور ضدا لغير المذكور لدلالة أحد الضدين على الآخر،",
     "en": "Whenever it is for detailing what was summarized, it must be repeated; but sometimes the mention of one division suffices, where what is mentioned is the contrary of what is not mentioned, since one of two contraries indicates the other,"},
    {"type": "matn",
     "ar": "كقوله تعالى: ﴿فأما الذين في قلوبهم زيغ فيتبعون ما تشابه﴾[[٣]]،",
     "en": "as in His words, the Exalted: “As for those in whose hearts is deviation, they follow what is ambiguous”;"},
    {"type": "matn",
     "ar": "فإن ما يقابل «أما» المذكورة ههنا غير مذكور، لكنه مقدر، يعني: «وأما الذين ليس في قلوبهم زيغ فيتبعون المحكمات، ويردون إليها المتشابهات»،",
     "en": "for what corresponds to the “ammā” mentioned here is not mentioned but is supposed, namely: “and as for those in whose hearts there is no deviation, they follow the unambiguous [verses] (al-muḥkamāt) and refer the ambiguous ones (al-mutashābihāt) back to them.”"},
    {"type": "matn",
     "ar": "والحكم بأن كلمة «أما» للشرط لزوم الفاء في جوابها، وسببية الأول للثاني.",
     "en": "The judgement that the word “ammā” is conditional rests on the fāʾ being required in its apodosis, and on the first being the cause of the second."},
    {"type": "matn",
     "ar": "(والتزم حذف فعلها) الذي هو الشرط (وعوض بينها) أي: بين «أما» (وبين فائها) الواقعة في جزائها (جزء مما في حيزها)",
     "en": "(Its verb is necessarily elided), the one that is the condition, (and in its place there is put, between it), that is, between “ammā”, (and its fāʾ), which occurs in its apodosis, (a part of what lies within its domain),"},
    {"type": "matn",
     "ar": "أي: حيز فائها أو حيز «أما»؛ لأن حيز الفاء أيضا حيزها،",
     "en": "that is, the domain of its fāʾ, or the domain of “ammā”, for the domain of the fāʾ is also its domain;"},
    {"type": "matn",
     "ar": "سواء كان ذلك الجزء مبتدأ نحو: «أما زيد فمنطلق» أو معمولا لما وقع بعد الفاء نحو: «أما يوم الجمعة فزيد منطلق»",
     "en": "whether that part is a subject (mubtadaʾ), as in “ammā Zaydun fa-munṭaliqun” (as for Zayd, he is departing), or governed by what comes after the fāʾ, as in “ammā yawma l-jumuʿati fa-Zaydun munṭaliqun” (as for Friday, Zayd is departing),"},
    {"type": "matn",
     "ar": "(مطلقا) أي: تعويضا مطلقا غير مقيد بحال تجويز تقديم ذلك الجزء على الفاء وعدم تجويزه.",
     "en": "(unrestrictedly), that is, an unrestricted substitution, not limited to the case where placing that part before the fāʾ is permitted or not permitted."},
    {"type": "matn",
     "ar": "وهذا مذهب سيبويه فجعل سيبويه ل«أما» خاصية جواز التقديم لما يمتنع تقديمه مطلقا.",
     "en": "This is the doctrine of Sībawayh; Sībawayh made it a special property of “ammā” that it permits placing first what otherwise cannot be placed first at all."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الحشر:١٢.",
     "en": "Qurʾān, Sūrat al-Ḥashr 59:12."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الأنعام:١٢١.",
     "en": "Qurʾān, Sūrat al-Anʿām 6:121."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "سورة آل عمران: ٧.",
     "en": "Qurʾān, Sūrat Āl ʿImrān 3:7."},
]
