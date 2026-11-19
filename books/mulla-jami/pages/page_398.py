# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 398 (printed ٣٩٧)."""

PAGE_NUMBER = 398
# REVIEW: the printed page number is faintly inked in the scan; read as «٣٩٧», consistent with the sequence.
PRINTED_PAGE = "٣٩٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «إذ في أخذ بعض الحروف من كل جزء مظنة» at the foot of PDF p. 397.
    {"type": "matn",
     "ar": "الالتباس، فاختاروا الأول ليدل على المقصود من أول الأمر،",
     "en": "…of confusion; so they chose the first, so that it would indicate what is meant from the very start."},
    {"type": "matn",
     "ar": "فأخذوا مثلا من «أحد عشر» المتضمن حرف العطف «حادي عشر» بمعنى الواحد من أحد عشر بشرط وقوعه بعد العشرة،",
     "en": "Thus, for example, from “aḥada ʿashara”, which contains the coordinating particle, they took “ḥādiya ʿashara”, meaning the one of eleven on condition that it comes after the ten;"},
    {"type": "matn",
     "ar": "فـ«حادي عشر» متضمن حرف العطف باعتبار أنه مأخوذ من «أحد عشر» المتضمن حرف العطف، لا باعتبار أن أصله: «حادي وعشر»؛ إذ لا معنى له،",
     "en": "so “ḥādiya ʿashara” contains the coordinating particle by virtue of being taken from “aḥada ʿashara”, which contains it, not by virtue of its origin being “ḥādin wa-ʿashrun”, since that has no meaning."},
    {"type": "matn",
     "ar": "وعلى هذا القياس «الحادي والعشرون» لا فرق بينهما إلا بذكر الواو وحذفه،",
     "en": "On this analogy is “al-ḥādī wa-l-ʿishrūn” (the twenty-first): there is no difference between the two except the mention of the wāw and its omission."},
    {"type": "matn",
     "ar": "(إلا «اثنى عشر») واثنتي عشرة»، فإنه لا يبنى فيهما الجزآن، بل يبنى الثاني للمتضمن، ويعرب الأول لشبهه بالمضاف لسقوط النون.",
     "en": "(Except “ithnā ʿashara”) and “ithnatay ʿashrata”: in these the two parts are not both indeclinable; rather the second is indeclinable because of what it contains, and the first is declinable because it resembles a construct noun (muḍāf), owing to the dropping of the nūn."},
    # REVIEW: the guillemets in «(إلا «اثنى عشر») واثنتي عشرة»» are printed as here (the second item has a closing mark only); transcribed as printed.
    {"type": "matn",
     "ar": "(وإلا) أي: وإن لم يتضمن الثاني حرفا (أعرب الثاني[[١]]) مع منع صرفه، إن لم يكن قبل التركيب مبنيا (كـ«بعلبك»، وبني الأول) للتوسط المانع من الإعراب، وعلى الفتح؛ لأنه أخف",
     "en": "(Otherwise), that is, if the second does not contain a particle, (the second is declinable), as a diptote, if it was not indeclinable before the combination, (as “Baʿlabakk”), (and the first is indeclinable), because of its medial position, which prevents inflection, and on fatḥa, because it is lightest,"},
    {"type": "matn",
     "ar": "(في الأفصح) أي: إعراب الثاني مع منع الصرف، وبناء الأول إنما هو في أفصح اللغات، وفيه لغتان أخريان:",
     "en": "(in the most eloquent usage), that is, the second’s being declinable as a diptote and the first’s being indeclinable is only in the most eloquent dialect. There are two other dialects in it:"},
    {"type": "matn",
     "ar": "إحداهما: إعراب الجزأين معا، وإضافة الأول إلى الثاني، ومنع صرف المضاف إليه.",
     "en": "one of them: both parts are declinable, the first annexed to the second, and the second (al-muḍāf ilayhi) diptote;"},
    {"type": "matn",
     "ar": "وأخراهما: إعراب الجزأين معا، وإضافة الأول إلى الثاني، وصرف الثاني.",
     "en": "and the other: both parts are declinable, the first annexed to the second, and the second fully declinable."},

    {"type": "section", "ar": "[الكنايات]",
     "en": "Allusive Nouns (al-Kināyāt)"},

    {"type": "matn",
     "ar": "(الكنايات) جمع كناية، وهي في اللغة والاصطلاح[[٢]]: أن يعبر عن شيء معين بلفظ غير صريح في الدلالة عليه، لغرض من الأغراض كالإبهام على السامعين،",
     "en": "(Allusive nouns): plural of kināya, which, in both lexical and technical usage, is to express a specific thing by an expression not explicit in signifying it, for some purpose, such as keeping it obscure from the hearers,"},
    {"type": "matn",
     "ar": "كقولك: «جاءني فلان» وأنت تريد «زيدا»،",
     "en": "as when you say “so-and-so (fulān) came to me”, meaning Zayd."},
    {"type": "matn",
     "ar": "والمراد بها ههنا ما يكنى به لا المعنى المصدري، ولا كل ما يكنى به بل بعضه، ولا كل بعض[[٣]]، بل بعض معين، فكأنهم",
     "en": "What is meant by it here is that by which allusion is made, not the verbal-noun sense; and not everything by which allusion is made, but some of it; and not any part, but a specific part; it is as if they…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فيه مسامحة، والمعنى أجري الإعراب على الثاني، وإلا فالمعرب بالإعراب الجاري على المركب هو مجموع المركب لا الجزء الثاني،",
     "en": "There is laxity in this; the meaning is that inflection is applied to the second, for otherwise what is inflected by the inflection running on the compound is the compound as a whole, not the second part."},
    {"type": "pair",
     "ar": "وقول الشارح: وإن لم يكن قبل التركيب مبنيا تقييد للحكم ليوافق ما هو المشهور والأولى،",
     "en": "The Commentator’s words “if it was not indeclinable before the combination” are a restriction of the ruling to make it agree with what is well known and preferable;"},
    {"type": "pair",
     "ar": "وإلا فقد نقل الرضي جواز إعراب الجزء الثاني المبني بعد التركيب كما هو ظاهر عبارة المصنف في هذا المقام، وفي بحث غير المنصرف،",
     "en": "otherwise, al-Raḍī reported that it is permissible to inflect the second part, [even if] indeclinable, after combination, as is the apparent sense of the Author’s wording in this place and in the discussion of the diptote."},
    {"type": "pair",
     "ar": "والأولى إن كان قابلا للإعراب مكان قوله: إن لم يكن مبنيا قبل التركيب؛ لأن كل اسم مبني قبل التركيب عند المصنف.",
     "en": "It would be better [to say] “if it is capable of inflection” in place of his words “if it was not indeclinable before the combination”, because every noun is indeclinable before combination according to the Author."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    # REVIEW: «يحاذبه» as printed (ḥāʾ, no dot); one would expect «يجاذبه» (as in al-Qāmūs). Transcribed as printed.
    {"type": "pair",
     "ar": "في القاموس: كنى به عن كذا، يكني ويكنو كناية: تكلم بما يستدل به عليه، أو أن تتكلم بشيء ويريد غيره، أو بلفظ يحاذبه جانبا حقيقة ومجاز.",
     "en": "In al-Qāmūs: kanā bihi ʿan kadhā, yaknī and yaknū, kināyatan: he spoke of something by which it is inferred; or it is that you speak of one thing and he means another; or [to speak] with an expression drawn between the two sides of literal and figurative meaning."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لا فرق بينه وبين كل ما يكنى به. والصواب: ولا بعض مبهم، وكأن السهو من الناسخ.",
     "en": "There is no difference between it and “everything by which allusion is made”. The correct reading is “and not an unspecified part”; it seems the slip is the copyist’s."},
]
