# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 315 (printed ٣١٤)."""

PAGE_NUMBER = 315
PRINTED_PAGE = "٣١٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(حملا) أي:» at the foot of PDF p. 314.
    {"type": "matn",
     "ar": "لمحموليته[[١]] (على «ضاربك») فاتحد فاعل المفعول له والفعل المعلل به، أعني: جاز،",
     "en": "…because it is assimilated (to “ḍāribuka”); so the agent of the object of purpose (mafʿūl lahu) and the verb explained by it, namely “was permitted,” are one."},
    {"type": "matn",
     "ar": "وبيانه: أنهم إذا وصلوا أسماء الفاعلين والمفعولين مجردة عن اللام بمفعولاتها، وكانت مضمرات متصلات، التزموا الإضافة ولم ينظروا إلى تحقق تخفيف،",
     "en": "The explanation of this: when they joined active and passive participles, bare of the article, to their objects, and these were attached pronouns, they made annexation obligatory and paid no regard to whether lightening was realized;"},
    {"type": "matn",
     "ar": "فقالوا: «الضاربك» وإن لم يحصل التخفيف بالإضافة، بل بنفس اتصال الضمير.",
     "en": "so they said “al-ḍāribuka,” although the lightening did not come about through annexation but through the attachment of the pronoun itself."},
    # REVIEW: the print reads «فقالوا: «الضاربك»» although the sentence concerns participles bare of the article; «ضاربك» would be expected; transcribed as printed.
    {"type": "matn",
     "ar": "ثم لما لم يعتبروا التخفيف في «ضاربك» وجوزوه بدونه، حملوا «الضاربك» عليه؛",
     "en": "Then, since they did not take lightening into account in “ḍāribuka” and permitted it without it, they assimilated “al-ḍāribuka” to it,"},
    {"type": "matn",
     "ar": "لأنهما من باب واحد حيث كان كل واحد منهما اسما فاعلا مضافا إلى مضمر متصل محذوفا تنوينه قبل الإضافة لا للإضافة،",
     "en": "because both belong to one category: each of them is an active participle annexed to an attached pronoun, its tanwīn having been dropped before annexation, not on account of annexation;"},
    {"type": "matn",
     "ar": "ولم يحملوا «الضارب زيد» عليه؛ لأنهما ليسا من باب واحد.",
     "en": "but they did not assimilate “al-ḍāribu Zaydin” to it, because the two do not belong to one category."},
    {"type": "matn",
     "ar": "والدليل على أن سقوط التنوين في «ضاربك» لاتصال الكاف لا للإضافة أنها لو سقطت للإضافة لكان ينبغي أن يتصور ذلك أولا على وجه يكون الضمير منصوبا بالمفعولية، ثم يضاف ويقال: «ضاربك»",
     "en": "The proof that the dropping of the tanwīn in “ḍāribuka” is due to the attachment of the kāf and not to annexation is that, had it dropped on account of annexation, one would have to conceive it first in a form in which the pronoun is accusative as object, and then it is annexed and one says “ḍāribuka,”"},
    {"type": "matn",
     "ar": "كما يتصور «ضارب زيدا»، ثم يضاف ويقال: «ضارب زيد»، ولن يتصور «ضاربك ك»، فعلم أنها سقطت لاتصال الكاف لا للإضافة.",
     "en": "just as “ḍāribun Zaydan” is conceived, and then it is annexed and one says “ḍāribu Zaydin”; but “ḍāribun ka” is never conceivable; so it is known that it dropped because of the attachment of the kāf, not because of annexation."},
    # REVIEW: the print reads «ضاربك ك» (with tanwīn on the first kāf and fatḥa on the detached kāf); the intended form appears to be «ضارب ك» (ḍāribun ka); transcribed as printed, diacritics dropped.
    {"type": "matn",
     "ar": "ولقائل أن يقول: لم لا يجوز أن يكون أصل ضاربك «ضارب إياك» للفصل بالتنوين، ثم لما أضيف حذف التنوين، وصار الضمير المنفصل متصلا، فصار «ضاربك»، وحصل التخفيف جدا،",
     "en": "Someone might say: why may the origin of “ḍāribuka” not be “ḍāribun iyyāka,” [with the detached pronoun] because of the separation by the tanwīn; then, when it was annexed, the tanwīn was dropped and the detached pronoun became attached, so it became “ḍāribuka,” and lightening was fully realized;"},
    {"type": "matn",
     "ar": "ثم حمل «الضاربك» عليه؛ لأنهما من باب واحد حيث كان كل واحد منهما اسما فاعلا مضافا إلى مضمر متصل من غير اعتبار حذف تنوينهما قبل الإضافة لا للإضافة،",
     "en": "then “al-ḍāribuka” was assimilated to it, because both belong to one category: each of them is an active participle annexed to an attached pronoun, without regard to their tanwīn having been dropped before annexation and not on account of it;"},
    {"type": "matn",
     "ar": "ولم يحملوا «الضارب زيد» عليه؛ لأنهما ليسا من باب واحد.",
     "en": "but they did not assimilate “al-ḍāribu Zaydin” to it, because the two do not belong to one category."},
    {"type": "matn",
     "ar": "واعلم أنا حملنا قوله: «وضعف: الواهب المائة الهجان وعبدها»، وقوله: «الضارب الرجل والضاربك» حملا على نظيريهما على الأجوبة عن استدلالات الفراء على جواز «الضارب زيد» عن جانب المصنف على موافقة بعض الشارحين،",
     "en": "Know that we have taken his words “and ‘al-wāhibu l-miʾati l-hijāni wa-ʿabdihā’ is weak” and his words “al-ḍāribu l-rajuli and al-ḍāribuka” as answers, on the author’s behalf, to al-Farrāʾ’s arguments for the permissibility of “al-ḍāribu Zaydin,” in agreement with some of the commentators;"},
    {"type": "matn",
     "ar": "ولك أن تجعل كل واحدة منها إشارة إلى مسألة على حدتها مناسبة للحكم بامتناع «الضارب زيد».",
     "en": "but you may take each of them as pointing to a separate question relevant to the ruling that “al-ḍāribu Zaydin” is impermissible."},
    {"type": "matn",
     "ar": "فمعنى قوله: «وضعف الواهب المائة الهجان وعبدها» أنه ضعف عطف المجرد عن اللام على المحلى به المضاف إليه صفة مصدرة بالام؛",
     "en": "Thus the meaning of his words “and ‘al-wāhibu l-miʾati l-hijāni wa-ʿabdihā’ is weak” is that it is weak to coordinate a noun bare of the article with a noun bearing it, to which an adjective headed by the article is annexed,"},
    # REVIEW: «بالام» as printed (for «باللام»); transcribed as printed.
    {"type": "matn",
     "ar": "لأنه بتوسط العطف يصير",
     "en": "because through the mediation of the coordination it becomes…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أو لحامليتهم له بناء على جعله مفعولا له للفعل المفهوم أي: جوزوا حملا.",
     "en": "Or because of their assimilating it, on the basis of taking it as the object of purpose of the verb that is understood, that is: they permitted it by way of assimilation."},
]
